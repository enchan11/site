import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. 페이지 기본 설정 및 구글 폰트 로드
st.set_page_config(page_title="오늘 뭐 입지? 🌤️", page_icon="✨", layout="centered")

# 동글동글하고 귀여운 폰트(부쿠 부쿠 또는 나눔스퀘어라운드 느낌)와 3D 스타일 CSS 적용
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Gamja+Flower&family=Gowun+Dodum&display=swap" rel="stylesheet">
    <style>
        /* 전체 폰트 및 배경 설정 */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Gowun Dodum', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
        }
        
        /* 제목 스타일 */
        .main-title {
            text-align: center;
            font-size: 2.8rem;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 5px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
        }
        .sub-title {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
        }

        /* 🔴 동글동글한 3D 뉴모피즘/클레이모피즘 카드 스타일 */
        .clay-card {
            background: #ffffff;
            border-radius: 24px;
            padding: 25px;
            box-shadow: inset 0px 4px 6px rgba(255, 255, 255, 0.6),
                        0px 15px 30px rgba(0, 0, 0, 0.06),
                        0px 4px 4px rgba(0, 0, 0, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.5);
            margin-bottom: 25px;
            transition: all 0.3s ease;
        }
        
        .clay-card:hover {
            transform: translateY(-5px);
            box-shadow: inset 0px 4px 6px rgba(255, 255, 255, 0.6),
                        0px 20px 40px rgba(0, 0, 0, 0.1);
        }

        /* 추천 텍스트 강조 */
        .recommend-text {
            font-size: 1.2rem;
            line-height: 1.8;
            color: #34495e;
        }
        
        .highlight {
            color: #ff6b6b;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 2. 귀여운 3D 모션 애니메이션을 가져오는 함수
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 부드러운 날씨/산책 관련 3D 스타일 애니메이션 주소
lottie_weather = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xl8aHg.json") # 귀여운 지구/날씨 모션

# 3. 메인 화면 구성
st.markdown("<h1 class='main-title'>오늘 뭐 입지? 🌤️</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>현재 온도에 딱 맞는 최적의 옷차림을 추천해 드려요</p>", unsafe_allow_html=True)

# 상단에 부드러운 애니메이션 배치
if lottie_weather:
    st_lottie(lottie_weather, height=200, key="weather_motion")

st.markdown("---")

# 4. 사용자 입력 인터페이스 (동글동글한 슬라이더와 선택창)
st.markdown("<div class='clay-card'>", unsafe_allow_html=True)
city = st.selectbox("📍 지역을 선택해 주세요", ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "제주"])
temp = st.slider("🌡️ 현재 기온을 설정해 주세요 (°C)", min_value=-10, max_value=35, value=18)
st.markdown("</div>", unsafe_allow_html=True)

# 5. 기온별 옷차림 추천 로직 및 결과 출력
st.markdown("### 👔 오늘의 추천 코디")

# 기온별 데이터를 부드러운 3D 느낌의 카드 안에 배치
card_content = ""

if temp >= 28:
    card_content = """
    ☀️ <b>28°C 이상 한여름 날씨예요!</b><br><br>
    가만히 있어도 땀이 주르륵 흐르는 날씨입니다. 최대한 얇고 통풍이 잘 되는 옷이 최고예요.<br>
    👉 <span class='highlight'>민소매, 반팔티, 반바지, 린넨 재질 옷, 원피스</span>를 추천합니다. 자외선 차단용 선글라스나 모자도 챙기세요!
    """
elif 23 <= temp < 28:
    card_content = """
    🌤️ <b>23°C ~ 27°C 초여름 날씨예요!</b><br><br>
    낮에는 꽤 더운 날씨입니다. 가벼운 옷차림이 활동하기 좋아요.<br>
    👉 <span class='highlight'>반팔티, 얇은 셔츠, 반바지, 면바지</span>가 딱 좋습니다. 외출 시 선크림은 필수!
    """
elif 20 <= temp < 23:
    card_content = """
    🍃 <b>20°C ~ 22°C 선선한 봄/가을이에요!</b><br><br>
    긴팔을 입기 딱 좋은 가장 쾌적한 날씨입니다.<br>
    👉 <span class='highlight'>블라우스, 긴팔티, 가벼운 셔츠, 슬랙스, 청바지</span>를 매치해 보세요.
    """
elif 17 <= temp < 20:
    card_content = """
    외출하기 딱 좋은 <b>17°C ~ 19°C</b> 입니다.<br><br>
    아침저녁으로는 약간 쌀쌀함을 느낄 수 있으니 입고 벗기 편한 겉옷이 유용합니다.<br>
    👉 <span class='highlight'>얇은 가디건, 니트, 맨투맨, 후드티, 청바지</span> 조합을 추천합니다.
    """
elif 12 <= temp < 17:
    card_content = """
    🍂 쌀쌀함이 느껴지는 <b>12°C ~ 16°C</b> 입니다.<br><br>
    본격적인 봄가을 날씨로, 자켓이나 도톰한 외투가 필요해요.<br>
    👉 <span class='highlight'>자켓, 가디건, 야상, 스타킹, 청바지, 면바지</span>를 입어 몸을 따뜻하게 해주세요.
    """
elif 9 <= temp < 12:
    card_content = """
    💨 찬 바람이 부는 <b>9°C ~ 11°C</b> 입니다.<br><br>
    꽤 춥게 느껴지므로 여러 겹을 레이어드해서 입는 것이 좋습니다.<br>
    👉 <span class='highlight'>트렌치코트, 야상, 점퍼, 도톰한 니트, 기모바지</span>를 추천합니다.
    """
elif 5 <= temp < 9:
    card_content = """
    🥶 초겨울 날씨인 <b>5°C ~ 8°C</b> 입니다.<br><br>
    감기 걸리기 딱 좋은 날씨니 외투에 신경 쓰셔야 합니다.<br>
    👉 <span class='highlight'>코트, 가죽자켓, 히트텍, 가벼운 패딩, 니트</span>로 무장하세요!
    """
else:
    card_content = """
    ❄️ <b>4°C 이하 한겨울 한파예요!</b><br><br>
    롱패딩은 패션이 아니라 생존입니다! 무조건 따뜻하게 입으세요.<br>
    👉 <span class='highlight'>패딩, 두꺼운 코트, 목도리, 장갑, 기모안감 옷, 히트텍</span> 필수 착용!
    """

# 커스텀 스타일 카드로 결과 렌더링
st.markdown(f"""
    <div class='clay-card recommend-text'>
        📍 <b>{city}</b>의 설정 온도: <b>{temp}°C</b><br><br>
        {card_content}
    </div>
""", unsafe_allow_html=True)

# 6. 하단 푸터 애니메이션
st.caption("✨ 디자인 팁: 모바일 화면에서도 3D 카드가 쫀득하게 반응합니다.")
