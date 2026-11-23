#!/bin/bash
# Gera a VSL leve para a página (720x1280, < 3 MB) e o poster, a partir de criativos/videos/com-audio/VSL_voz.mp4.
set -e
cd "$(dirname "$0")/../.."
IN=criativos/videos/com-audio/VSL_voz.mp4
OUT=criativos/videos/vsl
mkdir -p $OUT
# 2 passos com taxa-alvo: ~220 kb/s de vídeo + 64 kb/s de áudio -> ~2,9 MB em 85 s
ffmpeg -y -v error -i $IN -vf "scale=720:1280:flags=lanczos,fps=24" -c:v libx264 -preset slow -b:v 205k -pass 1 -passlogfile /tmp/vslpass -an -f mp4 /dev/null
ffmpeg -y -v error -i $IN -vf "scale=720:1280:flags=lanczos,fps=24" -c:v libx264 -preset slow -b:v 205k -pass 2 -passlogfile /tmp/vslpass \
  -profile:v high -pix_fmt yuv420p -c:a aac -b:a 64k -ar 48000 -ac 2 -movflags +faststart $OUT/vsl-ceia-720p.mp4
# poster: quadro da oferta (capa + preço), leve
ffmpeg -y -v error -ss 82 -i $IN -frames:v 1 -vf "scale=720:1280" -q:v 5 $OUT/vsl-poster.jpg
ls -la $OUT
