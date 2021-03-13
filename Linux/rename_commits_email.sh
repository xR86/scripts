#!/bin/sh

git filter-branch --env-filter '

OLD_EMAIL1="dan.alexandru@..."
OLD_EMAIL2="dan.alexandru2@..."
CORRECT_NAME="xR86"
CORRECT_EMAIL="9412441+xR86@users.noreply.github.com"

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL1" ] || [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL2" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi

if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL1" ] || [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL2" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
