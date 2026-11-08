# 영상 룩

출력: **16:9 · 1920×1080 · 30fps**. 아래 px는 최종 출력 캔버스 기준이다.
사용자 선택: **검정 배경 · 크고 꽉 찬 헤드라인 · 검정 엔드 카드** (2026-11-08 사용자 변경 요청).
색·폰트·원본 부품의 기준은 [design.md](design.md). 아래 `video-*`는 이 영상용 별칭이며 Figma 원본 변수는 아니다.
이 문서는 영상의 시각적 룩만 정의한다. 장면 순서·흐름·화면 구성은 레퍼런스와 영상별 비트 시트에서 정한다.
움직임·전환·타이밍은 [morion.md](../morion.md)를 참조한다.

## 1. 텍스트 최소 크기

| 토큰 | 값 | 기준 |
|---|---|---|
| `video-text-scale` | 2.8 | 사용자가 지정한 모션용 텍스트 배율 |
| `video-text-min` | 30.8px | `Text/eyebrow` 11px × 2.8 |
| `video-body-min` | 42px | `Text/body` 15px × 2.8 |

별도로 작성하는 영상 문구는 `video-text-min` 미만으로 줄이지 않는다. 본문·설명은 `video-body-min` 이상으로 쓴다.
글자가 넘치면 크기를 줄이거나 가로로 압축하지 않고 문구를 다듬거나 줄바꿈한다. 구체적인 줄바꿈과 위치는 비트 시트에서 정한다.
이 최소값은 모션용 문구 기준이다. 제품 화면 전체를 보여 주는 PNG 속 모든 UI 글자에 강제로 적용하지 않는다.
화면 속 정보를 실제로 읽혀야 한다면 해당 영역이나 HTML 부품을 확대해 최종 출력에서 최소 크기를 충족시킨다.

## 2. 배경

| 토큰 | 연결할 design 토큰 | 값 / 용도 |
|---|---|---|
| `video-bg` | `color-bg` | `#000000` · 사용자 지정 검정 바탕 |
| `video-surface` | `color-surface` | `#f7f7f8` · 부품과 구분할 보조 면 |
| `video-tint` | `color-primary-subtle` | `#edf1ff` · 브랜드 기운을 주는 밝은 면 |
| `video-end-bg` | `color-bg` | `#000000` · 엔드 카드 바탕 |
| `video-end-text` | `color-text` | `#ffffff` · 엔드 카드 문구 |

기본 바탕은 단색이다. 레퍼런스의 색·질감·사진 배경은 가져오지 않는다.
위 배경들은 선택 가능한 룩이며 사용 순서나 면적 비율을 뜻하지 않는다.
엔드 카드에는 기존 흰색 로고 SVG variant를 사용한다. 로고를 새로 그리거나 임의로 재색칠하지 않는다.

## 3. 글자

폰트는 **Pretendard**, 굵기는 원본의 **400 · 600 · 700**, 자간은 **0%**를 유지한다.
글자 크기는 Figma 값 × 2.8. 행간도 같은 배율을 적용해 원본의 비율을 유지한다. 소수점은 반올림하지 않는다.

| 토큰 | 원본 스타일 | 크기 / 행간 | 굵기 |
|---|---|---|---|
| `video-display` | `Text/display` | 78.4px / 95.2px | 700 |
| `video-title` | `Text/title` | 67.2px / 89.6px | 600 |
| `video-compact` | `Text/compact-title` | 61.6px / 78.4px | 700 |
| `video-section` | `Text/section` | 56px / 78.4px | 600 |
| `video-heading` | `Text/heading` | 50.4px / 78.4px | 600 |
| `video-body` | `Text/body` | 42px / 67.2px | 400 |
| `video-list` | `Text/list-title` | 42px / 61.6px | 600 |
| `video-label` | `Text/label` | 39.2px / 56px | 600 |
| `video-caption` | `Text/caption` | 33.6px / 44.8px | 400 |
| `video-eyebrow` | `Text/eyebrow` | 30.8px / 44.8px | 600 |

헤드라인의 기본은 `video-display`. ‘크고 꽉 차게’는 가장 큰 원본 스타일과 Bold를 선택하는 기준이다.
화면을 채우기 위해 2.8배를 초과하거나 글자를 늘이지 않는다. 여백·배치·줄 수는 이 문서에서 고정하지 않는다.

| 토큰 | 연결할 design 토큰 | 값 |
|---|---|---|
| `video-text` | `color-on-primary` | `#ffffff` |
| `video-muted` | `color-text-muted` | `#75777c` |
| `video-accent` | `color-primary` | `#3759de` |
| `video-on-accent` | `color-on-primary` | `#ffffff` |

핵심 문구는 `video-text`, 강조는 `video-accent`, 보조 표기만 `video-muted`를 쓴다.
`video-on-accent`는 브랜드색 면 위에 쓰는 글자색이다. 새 색이나 새로운 폰트 굵기를 추가하지 않는다.
폰트 파일은 `src/assets/fonts/Pretendard-{Regular,SemiBold,Bold}.otf`를 사용한다.
HTML 위치에 맞춰 경로를 연결하고 캡처·렌더 전에 `document.fonts.ready`를 기다린다.

## 4. 폰 프레임

사용자 요청(2026-11-08)에 따라 기본 2D 선 프레임을 **검정 정면 iPhone 목업**으로 교체했다.

- 자산: `src/assets/mockups/iphone-17e-black.webp` (Hoverify 제작, Apple 공식 자산 아님).
- 출처: https://tryhoverify.com/tools/device-frames/iphone-17e/
- 사용 조건: https://tryhoverify.com/tools/device-frames/license/ — 개인·상업 영상 사용 가능. 프레임 파일 자체의 재배포·판매 및 목업 도구 제공은 금지.
- 원본 프레임: 1326×2688px. 논리 크기: 442×896px (원본 ÷ 3).
- 화면 영역: 원본 기준 좌·상단 78px, 1170×2532px. 논리 기준 좌·상단 26px, 390×844px.
- 화면 모서리: 원본 141px, 논리 47px. 제공처 규격 그대로 사용한다.
- 기존 screens는 780×1688px이므로 ÷ 2로 화면 영역에 정확히 맞는다. 비균일 확대·내용 크롭 없이 원본 비율을 유지한다. 프레임의 모서리와 노치로 가리는 부분만 마스킹한다.
- 화면을 아래 레이어, 프레임을 위 레이어에 둔다. 기기 전체 이동·확대는 공통 래퍼로 처리한다. 부품을 밖으로 강조할 때는 기존 HTML을 별도 레이어로 사용한다.
- 노치·버튼·외곽은 목업 원본에 포함된 것을 사용한다. 새로 그리거나 임의 반사광·원근을 추가하지 않는다.

## 5. Parts

`src/parts/*.html`은 Figma 원본의 크기·여백·모서리·색·폰트·variant를 유지한다.
`video-part-scale`은 **독립 부품 강조용 기본 2.8**이다. 부품 전체를 래퍼로 균일 확대하므로 내부 글자도 같은 배율로 커진다.
이때 부품 내부 font-size에 2.8을 다시 곱하지 않는다. 350px 폭의 카드라면 출력 폭은 980px이며, 원본 HTML의 폭은 그대로 둔다.
폰 안의 UI에는 `video-part-scale`을 적용하지 않는다. 폰 래퍼의 배율을 따른다.
부품별 화면 크기·위치가 달라야 한다면 비트 시트에서 래퍼 배율을 지정하고, 읽어야 하는 글자의 최소 크기를 확인한다.
`asset-card.html`, `button-submit.html`의 상태는 기존 `data-state`를 사용한다. 영상용으로 원본 variant를 재디자인하지 않는다.
로고·일러스트·캐릭터는 `src/assets/` 원본을 감싸서 사용한다. 색·비율·형태를 바꾸지 않는다.
그림자가 필요하면 `design.md`의 기존 `Shadow/sm`, `Shadow/md`, `Shadow/lg` 중에서 선택하며 새 색·블러 값을 만들지 않는다.
`src/parts/_check/`의 비교 이미지는 검수용이며 영상 자산으로 쓰지 않는다.

## 6. OOS16 기반 수정 미리보기

새 사용자 요청에 따른 영상 전용 확대 타이포와 장면별 회전 제안은 `out/hurdling-club-intro/SPEC-v2.md`에 기록한다. 해당 v2 검토안에 한해 3장의 헤드라인 배율 제한을 확장한다. 제품 UI와 원본 자산에는 적용하지 않는다. 최종 룩 승인 대기.

### v2.1 사용자 지정
검정 기반 블루 그라데이션 허용(사용자 스크린샷 피드백). 설명 문구 확대와 엔딩 캐릭터 통일은 SPEC-v2.md의 v2.1 기준을 따른다. 이전 단색 제한보다 최신 사용자 요청을 우선한다.

### 강조 글자 밝기
사용자 가독성 피드백: v2 영상 헤드라인의 파란 글자에 한해 #6685ff를 사용한다. 제품 원본 UI의 color-primary는 유지한다.

### 현재 목업 업데이트
v2는 Hoverify iPhone 18 Pro Silver를 사용. 4장의17e 규격은 이전 버전용. 최신 규격·출처·화면 맞춤은 src/assets/mockups/SOURCE.md의 iPhone18Pro 항목 참조.
