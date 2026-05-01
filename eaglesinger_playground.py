#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EagleSinger One-File Playground
อ่าน/แสดงข้อมูลฟีเจอร์ 1–8 แบบอัตโนมัติในไฟล์เดียว
"""

import textwrap

README_TEXT = r"""
1. Chaos Mode Dashboard
   - หน้าคอนโซลรวมสวิตช์ URL, HTTPS, Proxy, IP, DNS, IPv4, IPv6, Gateway
   - Chaos Slider ระดับ 0–10 (0 = ปกติ, 10 = โกลาหลสุด)
   - Preset: Safe Flight / Storm Test / Blackout

2. License & Open Source Playground
   - สลับ License: MIT / Apache / GPL พร้อมคำอธิบายสั้น ๆ
   - Chaos License Mode: สุ่ม license (โหมดทดลอง)
   - Open Source Map: แผนภาพ dependency แบบ interactive

3. URL & HTTPS Trick Panel
   - HTTPS Flip: สลับ http ↔ https แล้วโชว์ผล secure / broken
   - Subdomain Mixer: api., dev., chaos. ฯลฯ
   - URL Inspector: แยก scheme / host / path / query เป็นบล็อกภาพ

4. Proxy & Gateway Chaos Lab
   - Proxy Chain Builder: ต่อ chain proxy แล้วดู latency จำลอง
   - Gateway Switch: เลือก gateway A/B/C แล้วกราฟ response เปลี่ยน
   - Geo-Route Simulator: เลือก IP/ประเทศ ดูเส้นทางทราฟฟิกคร่าว ๆ

5. IP / DNS / IPv4 / IPv6 Playground
   - DNS Resolver Visualizer: แสดงขั้นตอน query DNS ทีละ hop
   - IPv4 ↔ IPv6 Switch: สลับโหมดพร้อมตัวอย่าง address
   - IP Mask Slider: เลื่อน CIDR แล้วเห็นจำนวน host เปลี่ยน real-time

6. Mail & Notification Chaos
   - Security Alert Theme: โทนเมล Serious / Playful / Cyberpunk
   - Rate Limit Switch: Digest รายวัน vs แจ้งเตือนทันที
   - Test Mail Chaos: ทดสอบ TLS, DKIM/DMARC pass/fail จำลอง

7. Story of Chaos Mode
   - ทุกการเปลี่ยนสวิตช์มีข้อความเล่าเรื่อง เช่น
     "Eagle spreads its wings over IPv6-only sky."
     "DNS got confused and took the scenic route."

8. Safety Net & Reality Check
   - Global Kill Switch: รีเซ็ตกลับ preset ปลอดภัย
   - Sandbox Mode: ทุกอย่างเป็นการจำลอง ไม่แตะระบบจริง
   - Explain Button: ปุ่มอธิบายง่าย ๆ ข้างทุกสวิตช์ (ไทย/อังกฤษ)
"""

BANNER = r"""
╔══════════════════════════════════════════════╗
║        EagleSinger – Chaos Playground        ║
╚══════════════════════════════════════════════╝
"""

def parse_sections(text: str):
    sections = {}
    current = None
    body_lines = []

    for line in text.splitlines():
        stripped = line.strip()
        if stripped and stripped[0].isdigit() and stripped[1:3] == ". ":
            if current is not None:
                sections[current["index"]] = {
                    "title": current["title"],
                    "body": "\n".join(body_lines).strip(),
                }
                body_lines = []
            idx = int(stripped[0])
            title = stripped[3:].strip()
            current = {"index": idx, "title": title}
        else:
            if current is not None:
                body_lines.append(line)

    if current is not None:
        sections[current["index"]] = {
            "title": current["title"],
            "body": "\n".join(body_lines).strip(),
        }

    return sections


def render_menu(sections):
    print(BANNER)
    print("\n✨ ฟีเจอร์ที่มีในไฟล์นี้ (1–8):\n")
    for i in range(1, 9):
        sec = sections.get(i)
        if not sec:
            continue
        print(f"  [{i}] {sec['title']}")
    print("\nพิมพ์หมายเลขเพื่อดูรายละเอียด, หรือกด Enter เพื่อออก")


def show_section(sec):
    print("\n" + "=" * 60)
    print(f"{sec['title']}")
    print("=" * 60 + "\n")
    wrapped = textwrap.fill(sec["body"], width=80)
    print(wrapped)
    print("\n" + "=" * 60 + "\n")


def main():
    sections = parse_sections(README_TEXT)
    if not sections:
        print("ไม่พบข้อมูลหัวข้อ 1–8")
        return

    while True:
        render_menu(sections)
        choice = input("> ").strip()
        if not choice:
            break
        if not choice.isdigit():
            continue
        idx = int(choice)
        sec = sections.get(idx)
        if not sec:
            continue
        show_section(sec)


if __name__ == "__main__":
    main()
# Clone cd https://codespaces.new/anne1last-webpage/EagleSinger.Com?quickstart=1
python main.py
