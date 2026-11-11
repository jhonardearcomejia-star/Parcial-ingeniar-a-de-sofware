#!/usr/bin/env bash
# Crea el repo local, el commit del código heredado y la etiqueta v1.0.0
set -e
git init -b main
git add .
git commit -m "chore: código heredado EnvíaYa v1.0.0 con CONFIG personalizado"
git tag -a v1.0.0 -m "Código heredado v1.0.0"
git log --oneline --graph --all
