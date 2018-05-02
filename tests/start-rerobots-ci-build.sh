#!/bin/bash
# Launch new build on rerobots CI (https://ci.rerobots.net/)
#
# This script assumes the environment provided by Travis CI, in
# particular variables that declare the commit to use, etc.
# https://docs.travis-ci.com/user/environment-variables#Default-Environment-Variables
#
# There must be a rerobots API token in the env variable REROBOTS_API_TOKEN.
#
#
#
# SCL <scott@rerobots.net>
# Copyright (c) 2018 rerobots, Inc.
set -e

if [ $TRAVIS_PULL_REQUEST == "false" ]; then
    curl -X POST -H "Authorization: Bearer $REROBOTS_API_TOKEN" -d "{\"ns\": \"gh/${TRAVIS_REPO_SLUG}\", \"repo_url\": \"https://github.com/${TRAVIS_REPO_SLUG}.git\", \"repo_type\": \"git\", \"repo_branch\": \"${TRAVIS_BRANCH}\", \"repo_commit\": \"${TRAVIS_COMMIT}\"}" https://api.rerobots.net/ci/new
fi
