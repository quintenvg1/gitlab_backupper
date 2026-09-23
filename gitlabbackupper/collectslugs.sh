#!/usr/bin/env bash
set -euo pipefail

token=$(<token.txt)
base="https://gitlab.tailee6933.ts.net/api/v4/projects"
page=1
: > projectslugs.txt

while :; do
  resp=$(curl -sfk --header "PRIVATE-TOKEN: $token" \
    "$base?membership=true&simple=true&per_page=100&page=$page")

  [ "$(jq 'length' <<<"$resp")" -eq 0 ] && break

  jq -r '.[].ssh_url_to_repo' <<<"$resp" >> projectslugs.txt
  page=$((page + 1))
done

echo "Saved $(wc -l < projectslugs.txt) SSH URLs to projectslugs.txt"
