#!/bin/bash

# Retrieve and post-process the data
python3 retrieve-data.py

# Push
git config --global user.name "$GITHUB_ACTOR"
git config --global user.email "${GITHUB_ACTOR}@users.noreply.github.com"
git commit -a -m "Update data"
if [ $? -eq 0 ]; then
  git push
else
  echo "Data is latest, no need to commit"
fi
