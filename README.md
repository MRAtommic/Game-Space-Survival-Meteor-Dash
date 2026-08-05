# 🚀 Game-Space-Survival-Meteor-Dash

เกมแนว Arcade 2D พัฒนาด้วยภาษา Python และไลบรารี Pygame Zero โดยผู้เล่นจะได้รับบทเป็นผู้บังคับยานอวกาศ (UFO) ที่ต้องคอยหลบหลีกอุกกาบาตและลำแสงเลเซอร์ที่คอยขัดขวาง พร้อมทั้งเก็บสะสมเหรียญทำคะแนนให้ได้มากที่สุดก่อนหมดเวลา!

---

## ฟีเจอร์เด่นของเกม (Features)

* **ระบบระดับความยากตามเวลา (Dynamic Difficulty):** 
  * **Level 1 (Time > 40s):** ด่านเริ่มต้น ฉากหลังสีเทา 
  * **Level 2 (20s < Time <= 40s):** เพิ่มความตื่นเต้น ฉากหลังสีน้ำเงิน
  * **Level 3 (Time <= 20s):** ด่านสุดหิน ฉากหลังสีเขียว
* **ระบบควบคุมเพลงประกอบ:** สามารถเปิด/ปิดเพลงประกอบได้ตลอดเวลาขณะเล่น
* **ระบบ Game Over & Restart:** เมื่อชนสิ่งกีดขวางหรือหมดเวลา สามารถกด `ENTER` เพื่อเริ่มเล่นใหม่ได้ทันที

---

## การควบคุม (Controls)

| การกระทำ (Action) | ปุ่มกด (Key) |
| :--- | :--- |
| **เคลื่อนที่ขึ้น (Up)** | `W` |
| **เคลื่อนที่ลง (Down)** | `S` |
| **เคลื่อนที่ซ้าย (Left)** | `A` |
| **เคลื่อนที่ขวา (Right)** | `D` |
| **เล่นเพลงประกอบ (Play Music)** | `O` |
| **หยุดเพลงประกอบ (Stop Music)** | `P` |
| **เริ่มเล่นใหม่ (Restart Game)** | `ENTER` (เมื่อ Game Over) |

---

## ข้อกำหนดและสิ่งที่ต้องใช้ (Requirements)

* **Python 3.8** ขึ้นไป
* **Pygame Zero (`pgzero`)**

---

## การติดตั้งและการเริ่มใช้งาน (Setup & Installation)

1. **Clone หรือดาวน์โหลด repository นี้:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name

ติดตั้งไลบรารีที่จำเป็น:

```bash
pip install pgzero
   

วิธีที่ 1: รันผ่านคำสั่ง pgzrun

pgzrun game.py

วิธีที่ 2: รันผ่าน Python

Bash
python game.py

<img width="946" height="947" alt="image" src="https://github.com/user-attachments/assets/8b533b1e-de7e-4f42-bfe3-80b079b57fe4" />

<img width="572" height="750" alt="image" src="https://github.com/user-attachments/assets/afd750da-34c8-4c69-b39f-270d64a061d1" />


   
