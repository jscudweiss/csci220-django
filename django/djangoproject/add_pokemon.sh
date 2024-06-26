#!/bin/bash

set -euo pipefail

# Run migrations
# python3 manage.py flush --noinput && python3 manage.py makemigrations --empty pokedex ## DEBUG: DELETE ME LATER. THIS RESETS THE DATABASE EVERY TIME, TO ENSURE THAT THIS SCRIPT CAN RESURRECT IT
python3 manage.py makemigrations && python3 manage.py migrate

if python3 ./add_pokemon.py pokemon_are_added 
    then 
        echo "Database set up and filled with pokemon already"
        exit 0
fi

# # POKEMON TYPES # #

# Grab pokemon type chart data
curl https://gist.githubusercontent.com/chlohal/ee4667835256866d5d45c5729c0fdd1f/raw |
    # feed the CSV to the python script to add the types to the DB
    # The CSV I found uses ';' as a list separator, but it's easier on the Python if we 
    # use ' ', so `tr` it into a good format.
    tr ';' ' ' | 
    python3 ./add_pokemon.py poketypes

# # ABILITIES # #

curl https://gist.githubusercontent.com/chlohal/abaa991d3aaa88991d59485c962397c2/raw | 
    python3 ./add_pokemon.py pokeabilities



# # POKEMON # #

# Originally, this data was at https://www.kaggle.com/datasets/rounakbanik/pokemon
# However, it's CC0, and Kaggle is annoying to download from automatically, so I 
# mirrored the CSV to Github.
curl https://gist.githubusercontent.com/chlohal/94e668bbf5403eda4fa0420d7c9deb93/raw |
    # feed the CSV to the python script to add the 'mons to the DB
    # Skip the header line with `sed`
    sed '1d' | 
    # The abilities array can have embedded commas, so change its format to be semicolon-separated
    awk -F ']' -v OFS=']' '{gsub(/,/, ";", $1); print}' |
    # We only care about the first 650 pokemon (up to gen 5)
    awk -F ',' '$33 < 650' |
    python3 ./add_pokemon.py pokemon

# # POKEMON EVOLUTIONS # #

curl https://gist.githubusercontent.com/chlohal/db003077643332bd74e9738598ad443d/raw?asd |
    sed '1d' | 
    # We only care about the first 650 pokemon (up to gen 5)
    awk -F ',' '$1 < 650 && $2 < 650' | 
    python3 ./add_pokemon.py pokelutions

# # IMAGES # # 

# This makes `pokemon_images.tar.gz`
curl -o pokemon_images.tar.gz https://veekun.com/static/pokedex/downloads/generation-5.tar.gz

# Convert `pokemon_images.tar.gz` to `pokemon_images.tar`
# forcefully say "yes" to any confirmation prompts
gunzip -f pokemon_images.tar.gz

# untar `pokemon_images.tar` into the folder `pokemon`
tar -xf pokemon_images.tar

# feed pokemon image paths into the python script to add them to the db
# the script will figure out metadata from the paths, so no further
# effort needed
find pokemon -type f | python3 ./add_pokemon.py images

#Cleanup from this step
rm -rf pokemon pokemon_images.tar