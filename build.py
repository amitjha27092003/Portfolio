import base64
import os

b64_file = r'C:\Users\Dell\.gemini\antigravity\scratch\amit-portfolio-3d\profile_b64.txt'
with open(b64_file, 'r', encoding='utf-8') as f:
    b64_data = f.read().strip()

download_btn_exact = '''<a class="btn-p" href="assets/Amit_Kumar_Jha_Resume.pdf" download="Amit_Kumar_Jha_Resume.pdf" target="_blank" rel="noopener noreferrer">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="margin-right:8px;"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
  Download Updated CV
</a>'''

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Amit Kumar Jha — Operations &amp; AI Quality Assurance Professional</title>
  <meta name="description" content="Amit Kumar Jha - Versatile Operations and AI Quality Assurance Professional backed by over 3 years of enterprise workflow, prompt evaluation, and data validation experience.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #0b0f19;
      --bg-card: rgba(18, 24, 38, 0.75);
      --bg-card-hover: rgba(26, 34, 54, 0.9);
      --surface: #121826;
      --border: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(59, 130, 246, 0.45);
      --accent: #3b82f6;
      --accent-glow: rgba(59, 130, 246, 0.25);
      --accent-cyan: #06b6d4;
      --accent-purple: #8b5cf6;
      --accent-green: #10b981;
      --accent-amber: #f59e0b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-sub: #cbd5e1;
      --radius-sm: 10px;
      --radius-md: 16px;
      --radius-lg: 24px;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      -webkit-font-smoothing: antialiased;
      font-size: 16px;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      overflow-x: hidden;
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 15% 10%, rgba(59, 130, 246, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 85% 25%, rgba(139, 92, 246, 0.1) 0%, transparent 40%),
        radial-gradient(circle at 50% 70%, rgba(6, 182, 212, 0.08) 0%, transparent 45%);
      background-attachment: fixed;
    }}

    .bg-grid {{
      position: fixed;
      inset: 0;
      background-image: 
        linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
      background-size: 48px 48px;
      pointer-events: none;
      z-index: 0;
    }}

    .container {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 1;
    }}

    /* ==========================================================================
       HEADER & NAVIGATION
       ========================================================================== */
    header.site-header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 15, 25, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
    }}

    .nav-wrap {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 70px;
    }}

    .logo {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .logo-badge {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.12);
      border: 1px solid rgba(6, 182, 212, 0.3);
      padding: 2px 8px;
      border-radius: 6px;
    }}

    .nav-menu {{
      display: flex;
      align-items: center;
      gap: 8px;
      list-style: none;
    }}

    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      transition: color 0.2s ease, background-color 0.2s ease;
    }}

    .nav-link:hover {{
      color: #fff;
      background: rgba(255, 255, 255, 0.05);
    }}

    /* EXACT BUTTON STYLES FOR .btn-p */
    .btn-p {{
      background: linear-gradient(135deg, #2563eb, #3b82f6);
      color: #fff !important;
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 700;
      padding: 10px 20px;
      border-radius: 100px;
      display: inline-flex;
      align-items: center;
      border: 1px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 4px 14px var(--accent-glow);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      cursor: pointer;
    }}

    .btn-p:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 22px rgba(59, 130, 246, 0.45);
    }}

    /* ==========================================================================
       HERO SECTION
       ========================================================================== */
    .hero {{
      padding: 70px 0 60px;
      display: grid;
      grid-template-columns: 1fr 320px;
      gap: 48px;
      align-items: center;
    }}

    .hero-status-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.25);
      padding: 6px 14px;
      border-radius: 100px;
      font-size: 12.5px;
      font-weight: 600;
      color: #34d399;
      margin-bottom: 22px;
    }}

    .pulse-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      animation: pulseAnim 2s infinite ease-in-out;
    }}

    @keyframes pulseAnim {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      50% {{ transform: scale(1.2); opacity: 0.6; }}
    }}

    .hero-title {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: clamp(38px, 5.5vw, 56px);
      font-weight: 700;
      line-height: 1.1;
      letter-spacing: -1.5px;
      color: #fff;
      margin-bottom: 14px;
    }}

    .text-gradient {{
      background: linear-gradient(135deg, #60a5fa 0%, #38bdf8 50%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-headline {{
      font-size: 20px;
      font-weight: 600;
      color: var(--accent-cyan);
      margin-bottom: 14px;
      letter-spacing: -0.3px;
    }}

    .hero-summary {{
      font-size: 15.5px;
      color: var(--text-sub);
      line-height: 1.7;
      max-width: 620px;
      margin-bottom: 28px;
    }}

    .hero-contact-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 13.5px;
      color: var(--text-muted);
      margin-bottom: 30px;
    }}

    .contact-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .contact-item svg {{
      color: var(--accent);
    }}

    .hero-btn-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      align-items: center;
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-main);
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 600;
      padding: 10px 22px;
      border-radius: 100px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: 1px solid var(--border);
      transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
    }}

    .btn-secondary:hover {{
      background: rgba(255, 255, 255, 0.09);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-2px);
    }}

    /* ==========================================================================
       HERO AVATAR - GUARANTEED 100% VISIBLE WITH NEON BORDER
       ========================================================================== */
    .hero-avatar-card {{
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }}

    .avatar-neon-ring {{
      position: relative;
      width: 270px;
      height: 270px;
      border-radius: 50%;
      padding: 4px;
      background: linear-gradient(135deg, #3b82f6, #8b5cf6, #06b6d4, #10b981);
      box-shadow: 0 0 35px rgba(59, 130, 246, 0.35), 0 0 15px rgba(139, 92, 246, 0.2);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}

    .avatar-neon-ring:hover {{
      transform: scale(1.02);
      box-shadow: 0 0 45px rgba(59, 130, 246, 0.5), 0 0 25px rgba(6, 182, 212, 0.3);
    }}

    .avatar-inner {{
      width: 100%;
      height: 100%;
      border-radius: 50%;
      overflow: hidden;
      background: #111827;
      position: relative;
    }}

    .avatar-inner img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
    }}

    .avatar-badge {{
      position: absolute;
      bottom: -8px;
      left: 50%;
      transform: translateX(-50%);
      background: #1e293b;
      border: 1px solid var(--border-hover);
      color: #38bdf8;
      font-size: 11.5px;
      font-weight: 700;
      padding: 5px 14px;
      border-radius: 100px;
      white-space: nowrap;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* ==========================================================================
       KEY STATS
       ========================================================================== */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 70px;
    }}

    .stat-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px 18px;
      text-align: center;
      transition: border-color 0.25s ease, transform 0.25s ease;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
    }}

    .stat-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-3px);
    }}

    .stat-num {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 36px;
      font-weight: 700;
      line-height: 1;
      margin-bottom: 6px;
    }}

    .sc-blue {{ color: #60a5fa; }}
    .sc-purple {{ color: #a855f7; }}
    .sc-cyan {{ color: #22d3ee; }}
    .sc-emerald {{ color: #34d399; }}

    .stat-desc {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      line-height: 1.35;
    }}

    /* ==========================================================================
       SECTION COMMONS
       ========================================================================== */
    .section {{
      margin-bottom: 80px;
    }}

    .section-header {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 30px;
    }}

    .section-tag {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 13px;
      font-weight: 700;
      color: var(--accent-cyan);
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    .section-title {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 28px;
      font-weight: 700;
      color: #fff;
    }}

    .section-line {{
      flex: 1;
      height: 1px;
      background: linear-gradient(90deg, var(--border), transparent);
    }}

    /* ==========================================================================
       EXECUTIVE SUMMARY & COMPETENCIES
       ========================================================================== */
    .about-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 36px;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
    }}

    .about-p {{
      font-size: 16px;
      color: var(--text-sub);
      line-height: 1.8;
      margin-bottom: 28px;
    }}

    .about-p strong {{
      color: #fff;
    }}

    .competency-title {{
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--accent);
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .competency-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
    }}

    .competency-pill {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-sub);
      transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
    }}

    .competency-pill:hover {{
      background: rgba(59, 130, 246, 0.1);
      border-color: var(--border-hover);
      color: #fff;
      transform: translateX(4px);
    }}

    .competency-icon {{
      font-size: 16px;
    }}

    /* ==========================================================================
       WORK EXPERIENCE TIMELINE
       ========================================================================== */
    .timeline {{
      display: flex;
      flex-direction: column;
      gap: 24px;
      position: relative;
    }}

    .exp-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px;
      transition: border-color 0.2s ease, transform 0.2s ease;
    }}

    .exp-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }}

    .exp-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 14px;
      flex-wrap: wrap;
      margin-bottom: 6px;
    }}

    .exp-role {{
      font-size: 18px;
      font-weight: 700;
      color: #fff;
    }}

    .exp-badge {{
      font-size: 11.5px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 100px;
    }}

    .eb-active {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }}
    .eb-full {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }}
    .eb-contract {{ background: rgba(148, 163, 184, 0.15); color: #94a3b8; border: 1px solid rgba(148, 163, 184, 0.3); }}

    .exp-company {{
      font-size: 15px;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 4px;
    }}

    .exp-meta {{
      font-size: 13px;
      color: var(--text-muted);
      margin-bottom: 18px;
    }}

    .exp-bullets {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .exp-bullets li {{
      font-size: 14.5px;
      color: var(--text-sub);
      display: flex;
      align-items: flex-start;
      gap: 10px;
      line-height: 1.6;
    }}

    .bullet-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--accent);
      flex-shrink: 0;
      margin-top: 8px;
    }}

    /* ==========================================================================
       FEATURED PROJECTS (DIRECT LINKING TO LINKEDIN)
       ========================================================================== */
    .project-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 22px;
    }}

    a.project-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 26px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease, background-color 0.25s ease;
      position: relative;
      overflow: hidden;
    }}

    a.project-card:hover {{
      transform: translateY(-5px);
      border-color: var(--border-hover);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(59, 130, 246, 0.15);
      background: var(--bg-card-hover);
    }}

    .project-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}

    .project-type-tag {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--accent-cyan);
      background: rgba(6, 182, 212, 0.12);
      border: 1px solid rgba(6, 182, 212, 0.25);
      padding: 3px 10px;
      border-radius: 100px;
    }}

    .project-ext-icon {{
      color: var(--text-muted);
      transition: color 0.2s ease, transform 0.2s ease;
    }}

    a.project-card:hover .project-ext-icon {{
      color: #fff;
      transform: translate(2px, -2px);
    }}

    .project-title {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 10px;
      line-height: 1.35;
    }}

    .project-desc {{
      font-size: 14px;
      color: var(--text-sub);
      line-height: 1.6;
      margin-bottom: 20px;
      flex: 1;
    }}

    .project-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 14px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
    }}

    .project-link-text {{
      font-size: 13px;
      font-weight: 700;
      color: #60a5fa;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .linkedin-tag {{
      font-size: 11px;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.05);
      padding: 2px 8px;
      border-radius: 4px;
    }}

    /* ==========================================================================
       TECHNICAL SKILLS GRID
       ========================================================================== */
    .skills-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
    }}

    .skill-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 24px;
      transition: border-color 0.2s ease, transform 0.2s ease;
    }}

    .skill-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-3px);
    }}

    .skill-card-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 18px;
    }}

    .skill-icon-wrap {{
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: rgba(59, 130, 246, 0.12);
      color: #60a5fa;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
    }}

    .skill-category-title {{
      font-size: 16px;
      font-weight: 700;
      color: #fff;
    }}

    .skill-pills {{
      display: flex;
      flex-direction: column;
      gap: 9px;
    }}

    .skill-item {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      padding: 9px 12px;
      font-size: 13.5px;
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .skill-item-dot {{
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--accent-cyan);
    }}

    /* ==========================================================================
       EDUCATION & CERTIFICATIONS
       ========================================================================== */
    .edu-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
    }}

    .edu-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px;
      display: flex;
      gap: 20px;
      align-items: flex-start;
      transition: border-color 0.2s ease, transform 0.2s ease;
    }}

    .edu-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }}

    .edu-icon {{
      width: 52px;
      height: 52px;
      border-radius: 14px;
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(139, 92, 246, 0.2));
      border: 1px solid rgba(59, 130, 246, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
    }}

    .edu-inst {{
      font-size: 18px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 4px;
    }}

    .edu-degree {{
      font-size: 14.5px;
      font-weight: 600;
      color: var(--accent-cyan);
      margin-bottom: 4px;
    }}

    .edu-session {{
      font-size: 12.5px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}

    .edu-detail {{
      font-size: 13.5px;
      color: var(--text-sub);
      line-height: 1.6;
    }}

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    footer.site-footer {{
      padding: 60px 0 40px;
      border-top: 1px solid var(--border);
      text-align: center;
    }}

    .footer-name {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 32px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 8px;
    }}

    .footer-sub {{
      font-size: 14.5px;
      color: var(--text-muted);
      margin-bottom: 28px;
      max-width: 500px;
      margin-left: auto;
      margin-right: auto;
    }}

    .footer-actions {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 14px;
      margin-bottom: 36px;
      align-items: center;
    }}

    .footer-copy {{
      font-size: 12.5px;
      color: var(--text-muted);
    }}

    /* ==========================================================================
       RESPONSIVE DESIGN (MOBILE SMOOTH)
       ========================================================================== */
    @media (max-width: 860px) {{
      .hero {{
        grid-template-columns: 1fr;
        text-align: center;
        gap: 36px;
      }}
      .hero-avatar-card {{
        order: -1;
      }}
      .hero-contact-row {{
        justify-content: center;
      }}
      .hero-btn-row {{
        justify-content: center;
      }}
      .hero-summary {{
        margin-left: auto;
        margin-right: auto;
      }}
      .stats-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .nav-menu {{
        display: none;
      }}
    }}

    @media (max-width: 480px) {{
      .stats-grid {{
        grid-template-columns: 1fr;
      }}
      .hero-title {{
        font-size: 34px;
      }}
      .avatar-neon-ring {{
        width: 220px;
        height: 220px;
      }}
      .btn-p, .btn-secondary {{
        width: 100%;
        justify-content: center;
      }}
    }}
  </style>
</head>
<body>

  <div class="bg-grid"></div>

  <!-- Header -->
  <header class="site-header">
    <div class="container">
      <div class="nav-wrap">
        <a href="#top" class="logo">
          <span>Amit Kumar Jha</span>
          <span class="logo-badge">AI QA &amp; Ops</span>
        </a>

        <ul class="nav-menu">
          <li><a href="#about" class="nav-link">About</a></li>
          <li><a href="#experience" class="nav-link">Experience</a></li>
          <li><a href="#projects" class="nav-link">Featured Work</a></li>
          <li><a href="#skills" class="nav-link">Skills</a></li>
          <li><a href="#education" class="nav-link">Education</a></li>
        </ul>

        <div>
          {download_btn_exact}
        </div>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- ==========================================================================
         HERO SECTION
         ========================================================================== -->
    <section class="hero" id="top">
      <div>
        <div class="hero-status-pill">
          <span class="pulse-dot"></span>
          <span>Open to Opportunities · AI QA &amp; Operations Specialist · Noida / NCR</span>
        </div>

        <h1 class="hero-title">
          Amit Kumar <span class="text-gradient">Jha.</span>
        </h1>

        <div class="hero-headline">
          Versatile Operations &amp; AI Quality Assurance Professional
        </div>

        <p class="hero-summary">
          Over 3+ years of experience managing high-volume enterprise workflows, AI model evaluation, prompt quality benchmarking, data governance, and customer lifecycle operations.
        </p>

        <div class="hero-contact-row">
          <div class="contact-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            <span>Noida, Uttar Pradesh, India</span>
          </div>
          <div class="contact-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            <a href="mailto:ajha23275@gmail.com" style="color:inherit;text-decoration:none;">ajha23275@gmail.com</a>
          </div>
          <div class="contact-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <span>+91 8802449030</span>
          </div>
          <div class="contact-item">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            <a href="https://portfolio-fd7a.vercel.app" target="_blank" rel="noopener" style="color:inherit;text-decoration:none;">portfolio-fd7a.vercel.app</a>
          </div>
        </div>

        <div class="hero-btn-row">
          {download_btn_exact}
          <a href="https://www.linkedin.com/in/amit-jha-support" target="_blank" rel="noopener" class="btn-secondary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
            <span>LinkedIn Profile</span>
          </a>
          <a href="mailto:ajha23275@gmail.com" class="btn-secondary">
            <span>Email Me</span>
          </a>
        </div>
      </div>

      <!-- Avatar with Guaranteed Base64 Rendering & Neon Ring -->
      <div class="hero-avatar-card">
        <div class="avatar-neon-ring">
          <div class="avatar-inner">
            <img src="{b64_data}" alt="Amit Kumar Jha - Operations &amp; AI QA Professional" loading="eager">
          </div>
          <div class="avatar-badge">
            <span class="pulse-dot" style="width:6px;height:6px;"></span>
            <span>Ready to Scale</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         KEY STATS
         ========================================================================== -->
    <section class="stats-grid">
      <div class="stat-card">
        <div class="stat-num sc-blue">3+</div>
        <div class="stat-desc">Years Operations &amp; QA Experience</div>
      </div>
      <div class="stat-card">
        <div class="stat-num sc-purple">13+</div>
        <div class="stat-desc">Specialized AI Tasks Benchmarked</div>
      </div>
      <div class="stat-card">
        <div class="stat-num sc-cyan">100+</div>
        <div class="stat-desc">Monthly Escalations Resolved</div>
      </div>
      <div class="stat-card">
        <div class="stat-num sc-emerald">500+</div>
        <div class="stat-desc">LinkedIn Professional Network</div>
      </div>
    </section>

    <!-- ==========================================================================
         EXECUTIVE SUMMARY & COMPETENCIES
         ========================================================================== -->
    <section class="section" id="about">
      <div class="section-header">
        <span class="section-tag">Overview</span>
        <h2 class="section-title">Executive Summary</h2>
        <div class="section-line"></div>
      </div>

      <div class="about-card">
        <p class="about-p">
          Versatile Operations and AI Quality Assurance Professional backed by over 3 years of hands-on experience in managing high-volume enterprise workflows, customer lifecycle operations, and tech-driven data pipelines. Proven track record of bridging client success with modern tech solutions—leveraging prompt evaluation, data management tools, and process optimization to eliminate bottlenecks and scale operational efficiency. Backed by a strong technical foundation (BCA from Lovely Professional University) and deep expertise in AI-assisted automation, data validation, and CRM architectures.
        </p>

        <div class="competency-title">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          <span>Core Competencies &amp; Expertise</span>
        </div>

        <div class="competency-grid">
          <div class="competency-pill">
            <span class="competency-icon">🤖</span>
            <span>AI Model &amp; Prompt Evaluation</span>
          </div>
          <div class="competency-pill">
            <span class="competency-icon">📊</span>
            <span>Proposal Quality Benchmarking</span>
          </div>
          <div class="competency-pill">
            <span class="competency-icon">⚡</span>
            <span>Multi-channel Escalation Handling &amp; FCR/CSAT</span>
          </div>
          <div class="competency-pill">
            <span class="competency-icon">📈</span>
            <span>Advanced Excel (XLOOKUP, Pivot Tables, Dashboards)</span>
          </div>
          <div class="competency-pill">
            <span class="competency-icon">⚙️</span>
            <span>Workflow Automation &amp; Data Governance</span>
          </div>
          <div class="competency-pill">
            <span class="competency-icon">👥</span>
            <span>Cross-functional Leadership &amp; Training</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         WORK EXPERIENCE TIMELINE
         ========================================================================== -->
    <section class="section" id="experience">
      <div class="section-header">
        <span class="section-tag">Career</span>
        <h2 class="section-title">Work Experience</h2>
        <div class="section-line"></div>
      </div>

      <div class="timeline">
        <!-- Role 1 -->
        <div class="exp-card">
          <div class="exp-header">
            <div class="exp-role">AI Evaluation &amp; Quality Assurance Specialist</div>
            <span class="exp-badge eb-active">Project-Based · Current</span>
          </div>
          <div class="exp-company">Handshake AI</div>
          <div class="exp-meta">07/2026 – Present · Remote AI Fellowship</div>
          <ul class="exp-bullets">
            <li>
              <span class="bullet-dot"></span>
              <span>Executed rigorous AI model evaluations, proposal quality audits, and complex requirement verifications across 13+ specialized technical tasks.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Analyzed AI-generated logic and outputs against strict accuracy benchmarks, validating operational instructions to optimize system performance.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Partnered within collaborative tech workflows to assess prompt efficacy and streamline automated data validation pipelines.</span>
            </li>
          </ul>
        </div>

        <!-- Role 2 -->
        <div class="exp-card">
          <div class="exp-header">
            <div class="exp-role">Customer Support &amp; Operations Specialist</div>
            <span class="exp-badge eb-active">Current Role</span>
          </div>
          <div class="exp-company">BT Wave Solution Pvt Ltd</div>
          <div class="exp-meta">08/2025 – Present · Noida, Uttar Pradesh, India</div>
          <ul class="exp-bullets">
            <li>
              <span class="bullet-dot"></span>
              <span>Managed high-volume multichannel customer touchpoints (voice &amp; chat), consistently exceeding first-contact resolution (FCR) targets.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Maintained accurate records using internal tracking systems, ensuring real-time tracking of interactions and seamless CRM workflows.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Collaborated with engineering teams to isolate product bugs, translate user friction into technical requirements, and slash average handle times.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Maintained high customer satisfaction (CSAT) scores through empathetic, process-driven issue resolution and proactive communication.</span>
            </li>
          </ul>
        </div>

        <!-- Role 3 -->
        <div class="exp-card">
          <div class="exp-header">
            <div class="exp-role">Customer Care Executive</div>
            <span class="exp-badge eb-full">2 Years Full-Time</span>
          </div>
          <div class="exp-company">Tumbledry</div>
          <div class="exp-meta">07/2023 – 07/2025 · Noida, Uttar Pradesh, India</div>
          <ul class="exp-bullets">
            <li>
              <span class="bullet-dot"></span>
              <span>Acted as the primary escalation point for complex service requests, successfully orchestrating 100+ monthly client interactions.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Designed and implemented client retention workflows, tracking data insights via internal reporting tools to generate weekly performance reports.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Mentored and trained incoming support personnel on operational protocols, quality frameworks, and customer handling techniques.</span>
            </li>
          </ul>
        </div>

        <!-- Role 4 -->
        <div class="exp-card">
          <div class="exp-header">
            <div class="exp-role">Data Entry &amp; Back-Office Operations Clerk</div>
            <span class="exp-badge eb-contract">Operational Contract</span>
          </div>
          <div class="exp-company">ABC Solutions</div>
          <div class="exp-meta">07/2022 – 12/2022 · Remote</div>
          <ul class="exp-bullets">
            <li>
              <span class="bullet-dot"></span>
              <span>Managed high-throughput data processing systems using advanced Excel frameworks, ensuring zero-error data governance.</span>
            </li>
            <li>
              <span class="bullet-dot"></span>
              <span>Optimized internal documentation processes and streamlined record-keeping systems for the operations division.</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         FEATURED PROJECTS (DIRECT LINKING TO LINKEDIN)
         ========================================================================== -->
    <section class="section" id="projects">
      <div class="section-header">
        <span class="section-tag">Portfolio</span>
        <h2 class="section-title">Featured Projects &amp; Credentials</h2>
        <div class="section-line"></div>
      </div>

      <div class="project-grid">
        <!-- Project 1 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_ai-app-auracommand-autonomous-voice-ops-activity-7503035050595229697-IS2N" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">AI Application</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">AuraCommand — Autonomous Voice Ops AI</h3>
            <p class="project-desc">Voice-driven operational command interface engineered for automated task workflows and hands-free prompt execution.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>

        <!-- Project 2 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_handshake-aifellow-continuouslearning-activity-7499167061366075392-kJ6b" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">AI Quality Assurance</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">Handshake AI Fellow — Model &amp; Proposal Evaluation</h3>
            <p class="project-desc">Rigorous evaluation of LLM code generation, requirement audits, and prompt benchmarking for continuous AI learning.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>

        <!-- Project 3 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_robopotai-buildinpublic-ai-activity-7476586575250800640-nijn" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">Workflow Automation</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">Robopot AI — Conversational Intelligence</h3>
            <p class="project-desc">Autonomous conversational bot system designed for complex user intent resolution and multi-turn workflow management.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>

        <!-- Project 4 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_edtech-artificialintelligence-education-activity-7476563661483012098-0TfX" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">EdTech / AI Education</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">EduSphere AI — Hinglish Learning Platform</h3>
            <p class="project-desc">AI-assisted bilingual education platform simplifying core technical and competitive exam curricula for Indian students.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>

        <!-- Project 5 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_excel-dataanalytics-xlookup-activity-7442887362633908224-AKIb" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">Data Analytics</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">Enterprise Sales &amp; Banking Data Analysis</h3>
            <p class="project-desc">High-volume data modeling implementing nested XLOOKUPs, transactional error-handling, and automated commission calculations.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>

        <!-- Project 6 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_dataanalytics-excel-datavisualization-activity-7442532030971695104-KbwW" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">Business Intelligence</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">Interactive Executive KPI Dashboards</h3>
            <p class="project-desc">Multidimensional executive dashboard tracking KPIs, customer churn metrics, and revenue trends across dynamic chart types.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>

        <!-- Project 7 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_nptel-traininganddevelopment-professionalgrowth-activity-7078954019661955072-NMLV" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">Verified Certification</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">NPTEL / IIT Roorkee — Professional Training</h3>
            <p class="project-desc">12-week intensive corporate management and workflow development certification accredited with 72% aggregate score.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>

        <!-- Project 8 -->
        <a href="https://www.linkedin.com/posts/amit-jha-support_ethicalhacking-cybersecurity-computerscience-activity-7045613564438491136-dG56" target="_blank" rel="noopener" class="project-card">
          <div>
            <div class="project-top">
              <span class="project-type-tag">Technical Upskilling</span>
              <span class="project-ext-icon">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
              </span>
            </div>
            <h3 class="project-title">Ethical Hacking &amp; Cybersecurity Foundations</h3>
            <p class="project-desc">Comprehensive exploration of network security protocols, vulnerability discovery, and system integrity maintenance.</p>
          </div>
          <div class="project-footer">
            <span class="project-link-text">View on LinkedIn ↗</span>
            <span class="linkedin-tag">Post</span>
          </div>
        </a>
      </div>
    </section>

    <!-- ==========================================================================
         TECHNICAL SKILLS GRID
         ========================================================================== -->
    <section class="section" id="skills">
      <div class="section-header">
        <span class="section-tag">Skills</span>
        <h2 class="section-title">Technical &amp; Operational Stack</h2>
        <div class="section-line"></div>
      </div>

      <div class="skills-grid">
        <div class="skill-card">
          <div class="skill-card-header">
            <div class="skill-icon-wrap">🤖</div>
            <h3 class="skill-category-title">AI &amp; Prompt Engineering</h3>
          </div>
          <div class="skill-pills">
            <div class="skill-item"><span class="skill-item-dot"></span><span>AI Model Evaluation</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Prompt Quality Assessment</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Benchmark Audits &amp; Rubrics</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Low-Code Workflow Automation</span></div>
          </div>
        </div>

        <div class="skill-card">
          <div class="skill-card-header">
            <div class="skill-icon-wrap">📊</div>
            <h3 class="skill-category-title">Data &amp; Analytics</h3>
          </div>
          <div class="skill-pills">
            <div class="skill-item"><span class="skill-item-dot"></span><span>Advanced Excel (XLOOKUP, Pivots)</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Macros &amp; Dynamic Formulas</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Google Sheets &amp; Data Validation</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>SQL Queries &amp; Data Governance</span></div>
          </div>
        </div>

        <div class="skill-card">
          <div class="skill-card-header">
            <div class="skill-icon-wrap">⚡</div>
            <h3 class="skill-category-title">Operations &amp; CRM</h3>
          </div>
          <div class="skill-pills">
            <div class="skill-item"><span class="skill-item-dot"></span><span>Ticketing Workflows &amp; CRM</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Multichannel Support (Chat/Voice)</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Escalation Routing &amp; Resolution</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>CSAT &amp; FCR Management</span></div>
          </div>
        </div>

        <div class="skill-card">
          <div class="skill-card-header">
            <div class="skill-icon-wrap">💻</div>
            <h3 class="skill-category-title">Technical Background</h3>
          </div>
          <div class="skill-pills">
            <div class="skill-item"><span class="skill-item-dot"></span><span>Computer Science Principles (BCA)</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>DBMS &amp; Relational Architecture</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>Web Systems &amp; APIs</span></div>
            <div class="skill-item"><span class="skill-item-dot"></span><span>System QA &amp; Debugging</span></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==========================================================================
         EDUCATION & CERTIFICATIONS
         ========================================================================== -->
    <section class="section" id="education">
      <div class="section-header">
        <span class="section-tag">Education</span>
        <h2 class="section-title">Degrees &amp; Credentials</h2>
        <div class="section-line"></div>
      </div>

      <div class="edu-grid">
        <div class="edu-card">
          <div class="edu-icon">🎓</div>
          <div>
            <h3 class="edu-inst">Lovely Professional University (LPU)</h3>
            <div class="edu-degree">Bachelor of Computer Applications (BCA) — Computer Science</div>
            <div class="edu-session">Session: 2023 – 2026 · Currently Pursuing</div>
            <p class="edu-detail">
              Core focus on Database Management Systems (DBMS), Data Structures, Software Engineering, and Web Systems. Translating foundational computer science principles into scalable operations and AI QA pipelines.
            </p>
          </div>
        </div>

        <div class="edu-card">
          <div class="edu-icon">🏛️</div>
          <div>
            <h3 class="edu-inst">IIT Roorkee / NPTEL</h3>
            <div class="edu-degree">Training &amp; Development Certification Program (12-Week Intensive)</div>
            <div class="edu-session">Completed with 72% Aggregate Score · Distinction</div>
            <p class="edu-detail">
              Specialized in corporate workflow instruction, professional communication strategies, operational team mentoring, and customer lifecycle management.
            </p>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="site-footer" id="contact">
    <div class="container">
      <h3 class="footer-name">Amit Kumar Jha</h3>
      <p class="footer-sub">
        Versatile Operations &amp; AI Quality Assurance Professional<br>
        Noida, Uttar Pradesh, India · Open to High-Impact Opportunities
      </p>

      <div class="footer-actions">
        {download_btn_exact}
        <a href="https://www.linkedin.com/in/amit-jha-support" target="_blank" rel="noopener" class="btn-secondary">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
          <span>Connect on LinkedIn</span>
        </a>
        <a href="mailto:ajha23275@gmail.com" class="btn-secondary">
          <span>ajha23275@gmail.com</span>
        </a>
        <a href="tel:+918802449030" class="btn-secondary">
          <span>+91 8802449030</span>
        </a>
      </div>

      <p class="footer-copy">
        Designed for Amit Kumar Jha · Live Link: <a href="https://portfolio-fd7a.vercel.app" target="_blank" rel="noopener" style="color:var(--accent-cyan);text-decoration:none;">portfolio-fd7a.vercel.app</a>
      </p>
    </div>
  </footer>

</body>
</html>
"""

targets = [
    r'C:\Users\Dell\.gemini\antigravity\scratch\amit-portfolio-3d\index.html',
    r'C:\Users\Dell\Downloads\amit-portfolio-3d\index.html',
    r'C:\Users\Dell\Downloads\index.html'
]

for t in targets:
    with open(t, 'w', encoding='utf-8') as out:
        out.write(html_content)
    print(f'Wrote to {t} (bytes: {len(html_content)})')
