import streamlit as st
import os

# ====================== 【仅需修改这里：你的个人简历信息】 ======================
# 基础个人信息
NAME = "润松阁"
JOB_TITLE = "电脑基础培训师"
PHONE = "131-0000-5571"
EMAIL = "103045142985@qq.com"
GITHUB_URL = "https://github.com/rongsongge"
ADDRESS = "广东省广州市增城区新塘镇"

# 专业技能
SKILL_LIST = ["办公应用", "平面设计", "室内设计", "HTML/CSS/JS/Streamlit", "机电绘图", "视频剪辑"]

# 教学场景图片（图片放根目录，在此添加文件名，可多张）
TEACH_IMAGES = [
    "img1.jpg",
    "img2.jpg",
    "img3.jpg"
]

# 工作经历列表
WORK_EXPERIENCE = [
    {
        "company": "新塘成人文化技术学校",
        "position": "聘请教师",
        "time": "2000.03 - 2014.07",
        "desc": "• 电工考证班理论+实操教学\n• 模具专业CAD绘图课程授课\n• 电梯机械制图教学\n• 零基础电脑全科基础培训"
    },
    {
        "company": "新塘塘泽教育培训学校",
        "position": "聘请教师",
        "time": "2014.07 - 至今",
        "desc": "• 全套办公软件全科教学\n• PS/CDR/AI平面设计培训\n• CAD/3Dmax/酷家乐室内设计授课\n• SolidWorks/CAD机电绘图教学"
    }
]

# 项目介绍
PROJECT_NAME = "电脑全科一对一培训教学"
PROJECT_DESC = "常年开展小班一对一教学，单次辅导学员稳定15人左右，擅长零基础中老年、务工人员电脑入门教学"
# ==============================================================================

# 页面全局配置
st.set_page_config(
    page_title=f"{NAME} - 个人在线简历",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义页面CSS美化（增加手机自适应、标签优化）
st.markdown("""
<style>
.main {background-color: #f8f9fa;}
.block-container {padding-top: 2rem; padding-bottom: 2rem; max-width: 1200px; margin: 0 auto;}
.title-text {color: #2c3e50; font-weight: bold;}
.card {background: white; padding: 24px; border-radius: 12px; box-shadow: 0 2px 10px #e2e2e2; margin-bottom:24px}
.skill-tag {
    background:#3498db;color:white;padding:6px 14px;border-radius:24px;margin:6px 4px;display:inline-block;
    white-space:nowrap
}
@media screen and (max-width:768px){
    .block-container {padding: 1rem}
}
</style>
""", unsafe_allow_html=True)

# 资源全部放在根目录，无assets文件夹
avatar_path = "avatar.jpg"
audio_path = "bgm.mp3"
video_path = "work.mp4"

# 侧边栏：头像、背景音乐、基础信息
with st.sidebar:
    st.markdown("## 🧑 个人头像")
    try:
        st.image(avatar_path, width=200, caption="个人照片")
    except Exception:
        st.info("提示：把头像图片命名 avatar.jpg 放在项目根目录")

    st.markdown("## 🎵 背景音乐")
    try:
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
    except Exception:
        st.info("提示：背景音乐命名 bgm.mp3 放在项目根目录")

    st.divider()
    st.markdown(f"### {NAME}")
    st.markdown(f"**岗位：** {JOB_TITLE}")
    st.markdown(f"📞 电话：{PHONE}")
    st.markdown(f"📧 邮箱：{EMAIL}")
    st.markdown(f"📍 地址：{ADDRESS}")
    st.markdown(f"🐙 Github主页：[{NAME}]({GITHUB_URL})")

# 主页面标题
st.markdown(f"<h1 class='title-text'>📄 {NAME} 在线个人电子简历</h1>", unsafe_allow_html=True)
st.divider()

# 一、个人简介
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 👤 个人简介")
intro_text = """
本人深耕电脑职业培训行业二十余年，擅长零基础学员一对一辅导，覆盖青少年、务工人员、中老年等各类人群；
具备小班教学统筹经验，可独立负责20人以内同步教学，教学风格通俗易懂，配套实操案例，上手快。
"""
st.write(intro_text)
st.markdown("</div>", unsafe_allow_html=True)

# 二、专业技能
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 🛠️ 主讲培训课程")
skill_tags = ""
for skill in SKILL_LIST:
    skill_tags += f"<span class='skill-tag'>{skill}</span>"
st.markdown(skill_tags, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 新增：三、教学实景图片展示（放在工作经历前面）
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 🖼️ 教学实景实拍")
# 自动根据图片数量分列展示
if len(TEACH_IMAGES) > 0:
    cols = st.columns(len(TEACH_IMAGES))
    for idx, img_name in enumerate(TEACH_IMAGES):
        try:
            cols[idx].image(img_name, use_container_width=True, caption=f"教学场景 {idx+1}")
        except Exception:
            cols[idx].info(f"缺失图片：{img_name}，请放入项目根目录")
st.markdown("</div>", unsafe_allow_html=True)

# 四、工作经历
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 💼 从业工作经历")
for work in WORK_EXPERIENCE:
    st.subheader(f"{work['company']} | {work['position']}")
    st.caption(f"任职时间：{work['time']}")
    st.markdown(work['desc'])
    st.divider()
st.markdown("</div>", unsafe_allow_html=True)

# 五、项目视频展示（工作成果视频）
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 🎬 教学演示视频（教学成果）")
st.subheader(PROJECT_NAME)
st.write(PROJECT_DESC)
try:
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes)
except Exception:
    st.info("提示：教学视频命名 work.mp4 放在项目根目录")
st.markdown("</div>", unsafe_allow_html=True)

# 六、联系方式底部
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 📩 联系方式")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"**联系电话：** {PHONE}")
    st.markdown(f"**电子邮箱：** {EMAIL}")
with col2:
    st.markdown(f"**Github主页：** [{GITHUB_URL}]({GITHUB_URL})")
    st.markdown(f"**现居地址：** {ADDRESS}")
st.markdown("</div>", unsafe_allow_html=True)

# 页脚
st.caption("本电子简历由 Python + Streamlit 开发，支持免费云端部署，无任何费用")