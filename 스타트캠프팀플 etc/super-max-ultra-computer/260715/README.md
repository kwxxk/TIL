# LocalHub Busan — 프로젝트 안내

이 저장소는 로컬 정적 웹 뷰어(`localhub_busan.html`)와 간단한 번역 프록시 서버(`openai_translate_server.js`)를 포함합니다.

## 주요 파일
- `localhub_busan.html` — 메인 페이지(루트)
- `localhub/_busan.html` — 서버 경로용 복사본
- `부산_관광지.json`, `부산_문화시설.json`, `부산_쇼핑.json`, `부산_레포츠.json`, `부산_숙박.json`, `부산_축제공연행사.json`, `부산_여행코스.json` — 데이터 파일
- `openai_translate_server.js` — OpenAI 번역 프록시 (선택)
- `package.json` — Node 의존성 (번역 서버용)

## 실행 환경 (간단)
- 웹 브라우저(최신 Chrome/Edge 등)
- (번역 사용 시) Node.js (v16 이상 권장) 및 npm

## 빠른 시작 — 정적 모드 (권장)
1. 프로젝트 루트로 이동:
```bash
cd /path/to/260715
```
2. 간단한 정적 서버 실행 (Python 사용):
```bash
python -m http.server 8000
```
3. 브라우저에서 열기:
```
http://localhost:8000/localhub_busan.html
```

> 참고: 브라우저에서 로컬 `fetch()`로 JSON 파일을 불러오기 때문에 파일:// 경로로 열면 작동하지 않습니다.

## 번역 프록시 포함 모드 (선택)
번역 기능을 사용하려면 OpenAI API 키가 필요합니다.
1. Node 의존성 설치:
```bash
npm install
```
2. 루트에 `.env` 파일 생성(예):
```
OPENAI_API_KEY=sk-...
PORT=3000
```
3. 번역 서버 실행:
```bash
node openai_translate_server.js
```
4. 정적 서버 실행 (위와 같이)
5. 필요 시 `localhub_busan.html`의 `TRANSLATE_PROXY` 값을 번역 서버 주소로 변경하세요. 예:
```js
const TRANSLATE_PROXY = 'http://localhost:3000/translate';
```

## Google Maps
`localhub_busan.html` 내 `GOOGLE_MAPS_API_KEY` 변수에 키를 넣으면 Google Maps가 활성화됩니다. 키가 없으면 Leaflet로 자동 폴백됩니다.

## 네트워크 접근 (다른 PC에서 접속)
- 번역 서버(`PORT=3000`)와 정적 서버(`8000`)를 외부에서 접속하려면 해당 머신의 IP(예: `192.168.1.10`)를 사용하고 방화벽에서 포트를 열어야 합니다.
- 번역 서버는 `0.0.0.0`에 바인딩되어 있어 동일 LAN에서 접속 가능합니다.

## 배포/공유 권장 패키지
- 전달할 때는 루트 폴더 전체를 ZIP으로 압축하여 공유하세요. 꼭 포함해야 할 파일: `localhub_busan.html`, `localhub/_busan.html`, 모든 `부산_*.json`, `openai_translate_server.js`, `package.json`, `.env.example` (실제 키 제외).

## 문제 해결
- JSON 데이터가 로드되지 않으면 브라우저 콘솔의 네트워크 요청을 확인하세요(404 경로 문제).
- 번역이 실패하면 `openai_translate_server.js` 콘솔 로그와 `.env`의 API 키를 확인하세요.

---
필요하면 제가 `README.md`에 예시 `.env.example` 파일을 추가하거나, 프로젝트를 ZIP으로 묶어 드리겠습니다.
