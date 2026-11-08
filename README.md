# Huddling Club Motion

허들링 클럽의 스킬 탐색 → 미션 완료 → 검토·승인 → 내 자산 흐름을 담은 20초 제품 영상입니다.

- [최종 MP4](out/hurdling-club-intro/hurdling-club-final.mp4): 1920×1080, 30fps, H.264, 무음
- [렌더 확인 프레임](out/hurdling-club-intro/verification/final-sheet.png)
- [편집 소스](out/hurdling-club-intro/source/): HyperFrames 장면 5개와 GSAP 타임라인
- [제작 기록](out/hurdling-club-intro/SPEC-v2.md) · [렌더 검수](out/hurdling-club-intro/REVIEW-v2.md)

## 실행

Node.js, Python 3, 렌더용 FFmpeg가 필요합니다. 제작에 사용한 HyperFrames 버전은 0.9.21입니다.

```sh
python3 scripts/prepare_mockup.py
npx hyperframes@0.9.21 preview out/hurdling-club-intro/source --no-open --port 3017
```

미리보기 주소: `http://127.0.0.1:3017/#project/source`

```sh
# Homebrew가 설치된 macOS에서 FFmpeg 준비
brew install ffmpeg

npx hyperframes@0.9.21 render out/hurdling-club-intro/source \
  --output out/hurdling-club-intro/hurdling-club-final.mp4 \
  --quality delivery --fps 30 --workers 1 --experimental-fast-capture=false --strict
```

## 자산

제품 화면·부품·로고·폰트는 `src/`에 있습니다. 최종 영상에 사용한 Hoverify iPhone 18 Pro Silver 프레임은 완성 영상에 포함할 수 있지만 원본 파일 재배포가 제한되어 Git에 포함하지 않습니다. 준비 스크립트가 제공처에서 직접 다운로드합니다. [목업 출처와 사용 조건](src/assets/mockups/SOURCE.md)을 확인하세요.

`CLAUDE.md`, `.claude/agents/`, `skills/make-video/`는 이 프로젝트의 제작 절차입니다. 제작 기록의 로컬 절대 경로와 과거 버전 경로는 당시 환경의 기록이며, 현재 실행은 위 명령을 사용합니다.
