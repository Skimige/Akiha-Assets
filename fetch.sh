#!/bin/bash

curl $WAHLAP_SHOP_API_URL -o shop_data.json > /dev/null 2>&1
wget "$ALIAS_SHEET_TSV_URL" -O aliases.tsv > /dev/null 2>&1
git config --global user.name "$GITHUB_ACTOR"
git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"
git commit -a -m "Update data"
if [ $? -eq 0 ]; then
  git push
else
  echo "Data is latest, no need to commit"
fi
