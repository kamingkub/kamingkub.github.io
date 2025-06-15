import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# ตั้งค่าฟอนต์ภาษาไทย
rcParams['font.family'] = 'TH Sarabun New'
rcParams['font.size'] = 14
plt.rcParams['axes.unicode_minus'] = False

# อ่านข้อมูล CSV
df = pd.read_csv("country_wise_latest.csv")
df = df.dropna().drop_duplicates()

#เตรียมข้อมูลแปลชื่อประเทศเป็นภาษาไทย 
country_translation = {
    'USA': 'สหรัฐอเมริกา',
    'India': 'อินเดีย',
    'Brazil': 'บราซิล',
    'Russia': 'รัสเซีย',
    'Peru': 'เปรู',
    'Chile': 'ชิลี',
    'UK': 'สหราชอาณาจักร',
    'Mexico': 'เม็กซิโก',
    'Iran': 'อิหร่าน',
    'Spain': 'สเปน',
    'Italy': 'อิตาลี',
    'Germany': 'เยอรมนี',
    'Turkey': 'ตุรกี',
    'France': 'ฝรั่งเศส',
    'Colombia': 'โคลอมเบีย',
    'South Africa': 'แอฟริกาใต้',
    'Bangladesh': 'บังกลาเทศ',
    'Indonesia': 'อินโดนีเซีย',
    'Thailand': 'ประเทศไทย',
    'Argentina': 'อาร์เจนตินา',
    'United Kingdom' :'อังกฤษ'
}

# เลือกประเทศที่มีผู้ติดเชื้อมากที่สุด 10 อันดับ
top_countries = df.sort_values(by='Confirmed', ascending=False).head(10)

# แปลชื่อประเทศเป็นภาษาไทย
top_countries['Country/Region'] = top_countries['Country/Region'].replace(country_translation)

# เตรียมข้อมูล
country = top_countries['Country/Region']
infect = top_countries['Confirmed']
died = top_countries['Deaths']
curing = top_countries['Active']
cured = top_countries['Recovered']

x = np.arange(len(country))
width = 0.35

# สร้างกราฟ
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# ---------- กราฟที่ 1: รักษาอยู่ , หายแล้ว ----------
bar1 = axs[0].bar(x - width/2, curing, width, label='ผู้ป่วย (รักษาอยู่)', color='#f94144')
bar2 = axs[0].bar(x + width/2, cured, width, label='ผู้หายป่วย', color='#43aa8b')

axs[0].set_title('เปรียบเทียบจำนวนผู้ป่วยที่ยังรักษาอยู่และผู้หายป่วยจากโควิด-19 (10 ประเทศแรก)', fontsize=16)
axs[0].set_xlabel('ประเทศ', fontsize=13)
axs[0].set_ylabel('จำนวนคน', fontsize=13)
axs[0].set_xticks(x)
axs[0].set_xticklabels(country, rotation=45, ha='right')
axs[0].legend()
axs[0].grid(axis='y', linestyle='--', alpha=0.5)

axs[0].bar_label(bar1, padding=3, fontsize=10, labels=[f'{v:,}' for v in curing])
axs[0].bar_label(bar2, padding=3, fontsize=10, labels=[f'{v:,}' for v in cured])

# ---------- กราฟที่ 2: ติดเชื้อ , เสียชีวิต ----------
bar3 = axs[1].bar(x - width/2, infect, width, label='ผู้ติดเชื้อสะสม', color='#577590')
bar4 = axs[1].bar(x + width/2, died, width, label='ผู้เสียชีวิต', color='#bc4749')

axs[1].set_title('เปรียบเทียบจำนวนผู้ติดเชื้อสะสมและผู้เสียชีวิตจากโควิด-19 (10 ประเทศแรก)', fontsize=16)
axs[1].set_xlabel('country', fontsize=13)
axs[1].set_ylabel('จำนวนคน', fontsize=13)
axs[1].set_xticks(x)
axs[1].set_xticklabels(country, rotation=45, ha='right')
axs[1].legend()
axs[1].grid(axis='y', linestyle='--', alpha=0.5)

axs[1].bar_label(bar3, padding=3, fontsize=10, labels=[f'{v:,}' for v in infect])
axs[1].bar_label(bar4, padding=3, fontsize=10, labels=[f'{v:,}' for v in died])

plt.tight_layout()
plt.show()
