# JE Labs Pitch Deck — Web Presentation

## 📁 폴더 구조

```
jelabs-deck/
├── setup.py          ← 셋업 스크립트 (슬라이드 파일 → 배포 패키지 변환)
├── README.md         ← 이 파일
├── raw_slides/       ← 여기에 17개 슬라이드 HTML 파일을 넣으세요
│   ├── 01_cover.html
│   ├── 02_toc.html
│   ├── 03_who_we_are.html
│   ├── ...
│   └── 17_contact.html
└── dist/             ← (setup.py 실행 후 생성) 배포용 폴더
    ├── index.html    ← 메인 프레젠테이션 셸
    └── slides/
        ├── slide-0.html
        ├── slide-1.html
        └── ...
```

## 🚀 사용법

### Step 1: 슬라이드 파일 준비
`raw_slides/` 폴더를 만들고, 17개 슬라이드 HTML 파일을 순서대로 넣으세요.

파일 이름 앞에 번호를 붙이면 자동 정렬됩니다:
```
01_cover.html
02_table_of_contents.html  
03_section_who_we_are.html
04_growth_thesis.html
05_founder_profile.html
06_core_team.html
07_service_overview.html
08_gtm_strategy.html
09_founder_storytelling.html
10_media_thought_leadership.html
11_global_kol_network.html
12_developer_ecosystem.html
13_ambassador_program.html
14_community_growth.html
15_case_study_surf_ai.html
16_case_study_publicai.html
17_case_study_moss_ai.html
```

> ⚠️ Marketing Greenbooks와 Contact 슬라이드도 포함하려면 18, 19번으로 추가하세요.
> 그런 다음 `setup.py`에서 `TOTAL_SLIDES = 19`로 변경하면 됩니다.

### Step 2: 셋업 실행
```bash
python3 setup.py
```

### Step 3: 로컬 미리보기
```bash
cd dist
python3 -m http.server 8000
```
브라우저에서 `http://localhost:8000` 열기

> ⚠️ 로컬에서 직접 `index.html`을 열면 iframe CORS 문제가 생길 수 있습니다.
> 반드시 로컬 서버를 통해 열어주세요.

### Step 4: 배포

## 🌐 배포 플랫폼 추천

### 1. Netlify (가장 추천 ⭐)
- **무료**, 드래그 앤 드롭으로 배포 가능
- 커스텀 도메인 연결 쉬움
- HTTPS 자동 적용

**방법:**
1. [app.netlify.com/drop](https://app.netlify.com/drop) 접속
2. `dist/` 폴더를 드래그 앤 드롭
3. 끝! URL이 즉시 생성됩니다 (예: `jelabs-deck.netlify.app`)
4. 커스텀 도메인 연결: Site settings → Domain management

### 2. Vercel
- **무료**, CLI로 빠른 배포
- GitHub 연동 시 자동 배포

**방법:**
```bash
npm i -g vercel
cd dist
vercel
```

### 3. GitHub Pages
- **무료**, GitHub 계정만 있으면 됨

**방법:**
1. GitHub에 새 레포 생성 (예: `jelabs-deck`)
2. `dist/` 폴더 내용을 레포에 push
3. Settings → Pages → Source: "Deploy from a branch" → `main` 선택
4. URL: `https://yourusername.github.io/jelabs-deck/`

### 4. Cloudflare Pages
- **무료**, 글로벌 CDN으로 빠른 속도
- GitHub/GitLab 연동 지원

## ⌨️ 프레젠테이션 조작법

| 동작 | 키보드 | 마우스/터치 |
|------|--------|-------------|
| 다음 슬라이드 | `→` `↓` `Space` | 오른쪽 영역 클릭, 왼쪽 스와이프 |
| 이전 슬라이드 | `←` `↑` | 왼쪽 영역 클릭, 오른쪽 스와이프 |
| 처음으로 | `Home` | — |
| 마지막으로 | `End` | — |
| 풀스크린 | `F` | 풀스크린 버튼 클릭 |

## 🎨 커스터마이징

### 네온 컬러 변경
각 슬라이드 HTML에서 `#00F5B8`을 원하는 색상으로 교체하세요.

### 로고 변경
`https://www.genspark.ai/api/files/s/vZEsqoBT`를 자체 호스팅 로고 URL로 교체하세요.
배포 시에는 로고 파일을 `dist/` 폴더에 넣고 상대 경로로 참조하는 것을 추천합니다.

### 전환 효과 변경
`index.html`의 `.slide` CSS에서 `transition`과 `transform` 값을 수정하세요.

---
Built with ⚡ by JE Labs
