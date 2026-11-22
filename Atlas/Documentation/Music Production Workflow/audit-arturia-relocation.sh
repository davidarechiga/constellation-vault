#!/bin/zsh

# Read-only audit of the relocated Arturia product data.
# Columns: product, install files, resource files, cached VST3 executables.

set -u

arturia_root="/Library/Arturia"

if [[ ! -e "$arturia_root" ]]; then
  print -u2 "Missing: $arturia_root"
  exit 1
fi

printf 'product\tinstall_files\tresource_files\tvst3_executables\n'

for product_dir in "$arturia_root"/*; do
  [[ -d "$product_dir" ]] || continue
  product="${product_dir:t}"
  install_files=$(find "$product_dir/Install" -type f 2>/dev/null | wc -l | tr -d ' ')
  resource_files=$(find "$product_dir/resources" -type f 2>/dev/null | wc -l | tr -d ' ')
  vst3_executables=$(find "$product_dir/$product.vst3/Contents/MacOS" -type f 2>/dev/null | wc -l | tr -d ' ')
  printf '%s\t%s\t%s\t%s\n' "$product" "$install_files" "$resource_files" "$vst3_executables"
done
