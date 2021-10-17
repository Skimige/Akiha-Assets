#!/bin/bash

curl $WAHLAP_SHOP_API_URL -o shop_data.json > /dev/null
wget "$ALIAS_SHEET_TSV_URL" -O aliases.tsv > /dev/null
git config --global user.name 'Skimige'
git config --global user.email 'skimige@users.noreply.github.com'
git commit -a -m "Update data"
if [ $? -eq 0 ]; then
  git push
else
  echo "Data is latest, no need to commit"
fi
