#! /bin/bash

# Issues a batch download request; downloads to a file in the current
# directory.

url="https://ezid.cdlib.org/download_request"

if [ $# -lt 3 ]; then
  echo "Usage: batch-download.sh username password parameters..."
  echo
  echo "   format={anvl|csv|xml}                    required"
  echo "   compression={gzip|zip}                   defaults to gzip"
  echo "   column=c                                 repeatable"
  echo "      _id"
  echo "      _mappedCreator"
  echo "      _mappedTitle"
  echo "      _mappedPublisher"
  echo "      _mappedDate"
  echo "      _mappedType"
  echo "   notify=address                           repeatable"
  echo "   convertTimestamps={yes|no}"
  echo "   createdAfter={t|YYYY-MM-DDTHH:MM:SSZ}    inclusive"
  echo "   createdBefore={t|YYYY-MM-DDTHH:MM:SSZ}   exclusive"
  echo "   crossref={yes|no}"
  echo "   exported={yes|no}"
  echo "   owner=u                                  repeatable"
  echo "   ownergroup=g                             repeatable"
  echo "   permanence={test|real}"
  echo "   profile=p                                repeatable"
  echo "   status={reserved|public|unavailable}     repeatable"
  echo "   type={ark|doi|uuid}                      repeatable"
  echo "   updatedAfter={t|YYYY-MM-DDTHH:MM:SSZ}    inclusive"
  echo "   updatedBefore={t|YYYY-MM-DDTHH:MM:SSZ}   exclusive"
  exit
fi

echo "submitting download request..."
username="$1"; shift
password="$1"; shift
args=()
for a in "$@"; do
# add a '-d' before each parameter so that they are passed to the
# EZID API and joined on an ampersand.
  args+=("-d")
  args+=("$a")
done
# curl args -sS means -s: run silently without showing progress bar
# but -S do show errors. -u is for username & password
s="$(curl -sS -u "$username:$password" "${args[@]}" $url)"
if [ $? -ne 0 -o "${s:0:9}" != "success: " ]; then
  echo "$s"
  echo "request failed"
  exit 1
fi

echo -n "waiting.."
#success
url=${s:9:${#s}}
file=${url##*/}
status=22
# curl exit status 22 means HTTP page not retrieved. The requested url
# was not found or returned another error with the HTTP error code being
# 400 or above. This return code only appears if -f, --fail is used.
while [ $status -eq 22 ]; do
  echo -n "."
  sleep 5
  # curl args: -f indicates fail silently on server errors. -O tells curl
  # to write request output to a file in the current directory with the
  # same name as the file we're downloading. Overwrites existing files. -s
  # indicates don't show progress bar.
  curl -f -O -s $url
  status=$?
done
echo

if [ $status -eq 0 ]; then
  echo $file
else
  echo "download failed"
  echo "url: $url"
  exit 1
fi
