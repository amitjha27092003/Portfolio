/**
 * AMIT KUMAR JHA - 3D PORTFOLIO APPLICATION LOGIC
 * High-performance 3D tilt, theme switching, project modals & interactive effects
 */

// Project Showcase Detailed Data (8 Items)
const PROJECTS_DATA = [
  {
    id: "auracommand",
    title: "AuraCommand — Autonomous Voice Ops AI App",
    category: "ai",
    type: "AI Application / Autonomous Agents",
    shortDesc: "Voice-driven operational command interface engineered for automated task workflows and hands-free prompt execution.",
    fullDesc: "AuraCommand is an innovative autonomous voice operations platform designed to bridge spoken language intent with backend API execution. It provides operational teams with hands-free, voice-directed task orchestration, prompt chaining, and real-time execution monitoring.",
    highlights: [
      "Engineered autonomous voice-command pipeline translating natural speech into structured system actions.",
      "Built multi-turn intent resolution workflows with zero-latency speech-to-intent parsing.",
      "Designed prompt governance and security boundaries for enterprise operational execution.",
      "Demonstrated end-to-end task automation for customer operations and high-throughput workflows."
    ],
    tags: ["Voice AI", "Autonomous Agents", "Prompt Engineering", "Workflow Automation"],
    badgeColor: "#8b5cf6",
    link: "https://www.linkedin.com/posts/amit-jha-support_ai-app-auracommand-autonomous-voice-ops-activity-7503035050595229697-IS2N",
    svgIcon: "mic",
    gradient: "linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%)"
  },
  {
    id: "handshake-ai",
    title: "Handshake AI Fellow — Model & Proposal Evaluation",
    category: "ai",
    type: "AI Quality Assurance & Fellowship",
    shortDesc: "Rigorous evaluation of LLM code generation, requirement audits, and prompt benchmarking for continuous AI learning.",
    fullDesc: "As an AI Evaluation & QA Specialist with Handshake AI, executed intensive benchmarking and human-in-the-loop validation of frontier Large Language Models. Focused on code fidelity, instruction following, logic verification, and complex technical proposal quality assessments.",
    highlights: [
      "Audited 13+ specialized technical tasks evaluating LLM reasoning, code synthesis, and multi-step logic.",
      "Established strict accuracy rubrics and failure-mode taxonomies to continuously improve model output reliability.",
      "Validated prompt efficacy across diverse real-world enterprise scenarios and automated validation pipelines.",
      "Contributed to frontier model alignment through systematic comparative grading and feedback loops."
    ],
    tags: ["LLM Evaluation", "Benchmark Audits", "Prompt QA", "Data Validation"],
    badgeColor: "#3b82f6",
    link: "https://www.linkedin.com/posts/amit-jha-support_handshake-aifellow-continuouslearning-activity-7499167061366075392-kJ6b",
    svgIcon: "cpu",
    gradient: "linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%)"
  },
  {
    id: "robopot-ai",
    title: "Robopot AI — Conversational Intelligence & Workflow Automation",
    category: "ai",
    type: "Build in Public / AI Architecture",
    shortDesc: "Autonomous conversational bot system designed for complex user intent resolution and multi-turn workflow management.",
    fullDesc: "Robopot AI demonstrates an autonomous conversational architecture created to handle multi-turn dialogs, customer problem routing, and stateful workflow management. Developed openly in the 'Build in Public' community to explore conversational boundaries.",
    highlights: [
      "Constructed robust conversational decision trees and multi-turn contextual memory stores.",
      "Implemented automated intent classification to route users between self-service FAQs and escalation queues.",
      "Reduced simulated resolution times by over 40% using structured diagnostic flows.",
      "Documented architectural trade-offs between low-latency LLMs and deterministic rule engines."
    ],
    tags: ["Conversational AI", "Chatbot Architecture", "Intent Resolution", "BuildInPublic"],
    badgeColor: "#ec4899",
    link: "https://www.linkedin.com/posts/amit-jha-support_robopotai-buildinpublic-ai-activity-7476586575250800640-nijn",
    svgIcon: "bot",
    gradient: "linear-gradient(135deg, #3b0764 0%, #701a75 50%, #a21caf 100%)"
  },
  {
    id: "edusphere-ai",
    title: "EduSphere AI — EdTech Hinglish Learning Platform",
    category: "ai",
    type: "EdTech / AI Education",
    shortDesc: "AI-assisted bilingual education platform simplifying core technical and competitive exam curricula for Indian students.",
    fullDesc: "EduSphere AI is an educational concept and AI platform engineered specifically for students across India. By leveraging natural bilingual (Hinglish) explanations and contextual prompts, it breaks down complex computer science concepts, DBMS, and competitive exam modules into intuitive everyday analogies.",
    highlights: [
      "Customized bilingual prompting frameworks adapting technical terminology into conversational Hinglish.",
      "Integrated interactive quiz generation and real-time comprehension validation for students.",
      "Designed curriculum paths covering DBMS, computer science principles, and software development foundations.",
      "Demonstrated how culturally localized AI tutoring bridges the accessibility gap in tech education."
    ],
    tags: ["EdTech", "Bilingual AI", "Hinglish Prompting", "Accessible Learning"],
    badgeColor: "#10b981",
    link: "https://www.linkedin.com/posts/amit-jha-support_edtech-artificialintelligence-education-activity-7476563661483012098-0TfX",
    svgIcon: "book",
    gradient: "linear-gradient(135deg, #064e3b 0%, #065f46 50%, #047857 100%)"
  },
  {
    id: "sales-banking-analysis",
    title: "Enterprise Sales & Banking Data Analysis (XLOOKUP & Logic)",
    category: "data",
    type: "Data Analytics & Financial Operations",
    shortDesc: "High-volume data modeling implementing nested XLOOKUPs, transactional error-handling, and automated commission calculations.",
    fullDesc: "A comprehensive financial data analysis project built around banking transaction logs and sales agent performance data. Engineered utilizing advanced Microsoft Excel functions including multi-condition nested XLOOKUPs, dynamic range validation, and automated error-handling routines.",
    highlights: [
      "Processed multi-agent transaction datasets (TXN101–TXN104+) with zero calculation discrepancies.",
      "Implemented dynamic Data Validation dropdown lists connected seamlessly to automated commission lookups.",
      "Constructed transactional error-handling logic (IFERROR, ISBLANK) ensuring clean presentation of financial KPIs.",
      "Analyzed customer referral velocity and onboarding patterns across weekly operational batches."
    ],
    tags: ["Advanced Excel", "XLOOKUP", "Data Validation", "Financial Modeling"],
    badgeColor: "#f59e0b",
    link: "https://www.linkedin.com/posts/amit-jha-support_excel-dataanalytics-xlookup-activity-7442887362633908224-AKIb",
    svgIcon: "table",
    gradient: "linear-gradient(135deg, #451a03 0%, #78350f 50%, #92400e 100%)"
  },
  {
    id: "executive-kpi-dashboard",
    title: "Interactive Executive KPI Dashboards & Data Visualization",
    category: "data",
    type: "Business Intelligence / Excel",
    shortDesc: "Multidimensional executive dashboard tracking KPIs, customer churn metrics, and revenue trends across dynamic chart types.",
    fullDesc: "An executive-grade Business Intelligence dashboard developed in Excel featuring 6+ dynamic chart types, conditional formatting heatmaps, and weekly performance summaries. Designed to give C-suite decision-makers instant visibility into operational bottlenecks, referral shifts, and revenue trends.",
    highlights: [
      "Engineered 3D column charts, horizontal bar comparisons, area graphs, and radar performance spider charts.",
      "Applied conditional formatting heatmaps flagging underperforming operational cohorts in real time.",
      "Built interactive weekly referral share analysis across 99+ transaction cohorts.",
      "Automated weekly executive reporting reducing manual chart generation time from hours to minutes."
    ],
    tags: ["BI Dashboards", "Pivot Tables", "Data Visualization", "Executive Reporting"],
    badgeColor: "#0284c7",
    link: "https://www.linkedin.com/posts/amit-jha-support_dataanalytics-excel-datavisualization-activity-7442532030971695104-KbwW",
    svgIcon: "chart",
    gradient: "linear-gradient(135deg, #082f49 0%, #0369a1 50%, #0284c7 100%)"
  },
  {
    id: "iit-roorkee-nptel",
    title: "NPTEL / IIT Roorkee — Professional Training & Development",
    category: "cert",
    type: "Verified Certification",
    shortDesc: "12-week intensive corporate management and workflow development certification accredited with 72% aggregate score.",
    fullDesc: "Completed a comprehensive 12-week executive certification program conducted by the Indian Institute of Technology (IIT) Roorkee and NPTEL. The program focused on strategic operational frameworks, organizational leadership, corporate workflow instruction, and advanced conflict management.",
    highlights: [
      "Graduated with Distinction, achieving a 72% aggregate score in final proctored evaluations.",
      "Mastered corporate communication strategies, operational team mentoring, and training program design.",
      "Applied modern organizational management paradigms directly to support and operations team workflows.",
      "Endorsed by Ministry of Education (Govt. of India) and IIT Roorkee academic leadership."
    ],
    tags: ["IIT Roorkee", "NPTEL", "Training & Development", "Leadership"],
    badgeColor: "#6366f1",
    link: "https://www.linkedin.com/posts/amit-jha-support_nptel-traininganddevelopment-professionalgrowth-activity-7078954019661955072-NMLV",
    svgIcon: "award",
    gradient: "linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%)"
  },
  {
    id: "cybersecurity-foundations",
    title: "Ethical Hacking & Cybersecurity Foundations",
    category: "cert",
    type: "Technical Upskilling",
    shortDesc: "Comprehensive exploration of network security protocols, vulnerability discovery, and system integrity maintenance.",
    fullDesc: "Extensive study and hands-on lab experimentation covering the foundations of ethical hacking, defensive cybersecurity architectures, network protocol analysis, and enterprise data integrity protection.",
    highlights: [
      "Conducted network reconnaissance and port analysis using standard diagnostic tools.",
      "Explored common web vulnerability vectors (OWASP Top 10) including SQL injection and XSS defenses.",
      "Gained working understanding of data governance, cryptographic handshakes, and access control policies.",
      "Applied defensive security principles to enterprise CRM workflows and data validation pipelines."
    ],
    tags: ["Cybersecurity", "Network Protocols", "Ethical Hacking", "Data Integrity"],
    badgeColor: "#ef4444",
    link: "https://www.linkedin.com/posts/amit-jha-support_ethicalhacking-cybersecurity-computerscience-activity-7045613564438491136-dG56",
    svgIcon: "shield",
    gradient: "linear-gradient(135deg, #450a0a 0%, #7f1d1d 50%, #991b1b 100%)"
  }
];

// SVG Icon Generator Helper for Visual Banners
function getSvgVisual(type, title) {
  switch (type) {
    case "mic":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="auraglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.6"/>
              <stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#0d1127"/>
          <circle cx="180" cy="90" r="75" fill="url(#auraglow)"/>
          <path d="M60 90 Q 120 50 180 90 T 300 90" fill="none" stroke="#8b5cf6" stroke-width="2.5" opacity="0.5"/>
          <path d="M40 90 Q 110 130 180 90 T 320 90" fill="none" stroke="#3b82f6" stroke-width="2.5" opacity="0.5"/>
          <path d="M90 90 Q 135 30 180 90 T 270 90" fill="none" stroke="#c084fc" stroke-width="3"/>
          <rect x="166" y="55" width="28" height="46" rx="14" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
          <path d="M154 78 C 154 96 206 96 206 78" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="180" y1="102" x2="180" y2="120" stroke="#ffffff" stroke-width="2.5"/>
          <line x1="168" y1="120" x2="192" y2="120" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
          <text x="180" y="152" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#93c5fd" text-anchor="middle" letter-spacing="2">AURACOMMAND • VOICE OPS AI</text>
        </svg>
      `;
    case "cpu":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="cpuglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.5"/>
              <stop offset="100%" stop-color="#1e3a8a" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#090d1f"/>
          <circle cx="180" cy="85" r="70" fill="url(#cpuglow)"/>
          <line x1="120" y1="85" x2="70" y2="85" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4 4"/>
          <line x1="240" y1="85" x2="290" y2="85" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4 4"/>
          <line x1="180" y1="40" x2="180" y2="15" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4 4"/>
          <line x1="180" y1="130" x2="180" y2="155" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4 4"/>
          <rect x="145" y="50" width="70" height="70" rx="14" fill="#1e293b" stroke="#60a5fa" stroke-width="2.5"/>
          <path d="M165 72 L176 85 L196 68" fill="none" stroke="#34d399" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="180" y="106" font-family="'Outfit', sans-serif" font-size="9" font-weight="800" fill="#94a3b8" text-anchor="middle">BENCHMARK QA</text>
          <text x="180" y="162" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#60a5fa" text-anchor="middle" letter-spacing="2">HANDSHAKE AI FELLOW</text>
        </svg>
      `;
    case "bot":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="botglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#ec4899" stop-opacity="0.4"/>
              <stop offset="100%" stop-color="#701a75" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#160822"/>
          <circle cx="180" cy="85" r="70" fill="url(#botglow)"/>
          <rect x="145" y="48" width="70" height="60" rx="16" fill="#2e1065" stroke="#f472b6" stroke-width="2.5"/>
          <circle cx="166" cy="74" r="5" fill="#38bdf8"/>
          <circle cx="194" cy="74" r="5" fill="#38bdf8"/>
          <path d="M166 92 Q 180 100 194 92" fill="none" stroke="#f472b6" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="180" y1="48" x2="180" y2="34" stroke="#f472b6" stroke-width="2"/>
          <circle cx="180" cy="32" r="3.5" fill="#f43f5e"/>
          <text x="180" y="152" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#f472b6" text-anchor="middle" letter-spacing="2">ROBOPOT AI • CONVERSATIONAL</text>
        </svg>
      `;
    case "book":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="eduglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#10b981" stop-opacity="0.45"/>
              <stop offset="100%" stop-color="#064e3b" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#051914"/>
          <circle cx="180" cy="85" r="70" fill="url(#eduglow)"/>
          <path d="M140 68 Q 180 55 180 110 Q 140 98 140 68 Z" fill="#065f46" stroke="#34d399" stroke-width="2"/>
          <path d="M220 68 Q 180 55 180 110 Q 220 98 220 68 Z" fill="#047857" stroke="#34d399" stroke-width="2"/>
          <line x1="180" y1="58" x2="180" y2="114" stroke="#a7f3d0" stroke-width="2.5"/>
          <text x="180" y="152" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#34d399" text-anchor="middle" letter-spacing="2">EDUSPHERE AI • HINGLISH EDTECH</text>
        </svg>
      `;
    case "table":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="excelglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.45"/>
              <stop offset="100%" stop-color="#78350f" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#1a1103"/>
          <circle cx="180" cy="85" r="70" fill="url(#excelglow)"/>
          <rect x="135" y="44" width="90" height="66" rx="8" fill="#291b07" stroke="#fbbf24" stroke-width="2"/>
          <line x1="135" y1="62" x2="225" y2="62" stroke="#fbbf24" stroke-width="1.5"/>
          <line x1="135" y1="80" x2="225" y2="80" stroke="#fbbf24" stroke-width="1"/>
          <line x1="135" y1="96" x2="225" y2="96" stroke="#fbbf24" stroke-width="1"/>
          <line x1="165" y1="44" x2="165" y2="110" stroke="#fbbf24" stroke-width="1.5"/>
          <line x1="195" y1="44" x2="195" y2="110" stroke="#fbbf24" stroke-width="1"/>
          <text x="180" y="152" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#fcd34d" text-anchor="middle" letter-spacing="2">XLOOKUP & BANKING LOGIC</text>
        </svg>
      `;
    case "chart":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="chartglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#0ea5e9" stop-opacity="0.45"/>
              <stop offset="100%" stop-color="#0369a1" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#051421"/>
          <circle cx="180" cy="85" r="70" fill="url(#chartglow)"/>
          <line x1="120" y1="110" x2="240" y2="110" stroke="#38bdf8" stroke-width="1.5"/>
          <rect x="135" y="70" width="18" height="40" rx="3" fill="#38bdf8"/>
          <rect x="160" y="50" width="18" height="60" rx="3" fill="#0284c7"/>
          <rect x="185" y="80" width="18" height="30" rx="3" fill="#f43f5e"/>
          <rect x="210" y="58" width="18" height="52" rx="3" fill="#10b981"/>
          <path d="M144 65 L 169 45 L 194 75 L 219 52" fill="none" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="169" cy="45" r="3.5" fill="#fef08a"/>
          <text x="180" y="152" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle" letter-spacing="2">KPI DASHBOARD & 3D CHARTS</text>
        </svg>
      `;
    case "award":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="awardglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#6366f1" stop-opacity="0.5"/>
              <stop offset="100%" stop-color="#312e81" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#0b0a1f"/>
          <circle cx="180" cy="80" r="70" fill="url(#awardglow)"/>
          <circle cx="180" cy="70" r="28" fill="#1e1b4b" stroke="#818cf8" stroke-width="2.5"/>
          <polygon points="180,52 186,65 200,66 189,76 192,90 180,82 168,90 171,76 160,66 174,65" fill="#fbbf24"/>
          <path d="M170 94 L162 120 L176 112 L190 120 L182 94" fill="#4338ca" stroke="#818cf8" stroke-width="1.5"/>
          <text x="180" y="152" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#a5b4fc" text-anchor="middle" letter-spacing="2">IIT ROORKEE • NPTEL CERTIFIED</text>
        </svg>
      `;
    case "shield":
      return `
        <svg viewBox="0 0 360 180" class="g-svg-canvas" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="shieldglow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#ef4444" stop-opacity="0.45"/>
              <stop offset="100%" stop-color="#7f1d1d" stop-opacity="0"/>
            </radialGradient>
          </defs>
          <rect width="100%" height="100%" fill="#1f0707"/>
          <circle cx="180" cy="80" r="70" fill="url(#shieldglow)"/>
          <path d="M180 44 L 212 56 C 212 90 180 114 180 114 C 180 114 148 90 148 56 Z" fill="#450a0a" stroke="#f87171" stroke-width="2.5"/>
          <path d="M174 74 L 180 68 L 186 74" fill="none" stroke="#fca5a5" stroke-width="2" stroke-linecap="round"/>
          <rect x="172" y="74" width="16" height="14" rx="3" fill="#f87171"/>
          <text x="180" y="152" font-family="'Outfit', sans-serif" font-size="11" font-weight="700" fill="#fca5a5" text-anchor="middle" letter-spacing="2">ETHICAL HACKING & CYBERSECURITY</text>
        </svg>
      `;
    default:
      return `<div style="background:var(--bg2);width:100%;height:100%;"></div>`;
  }
}

// Render Project Cards dynamically
function renderProjects(filter = "all") {
  const grid = document.getElementById("projects-grid");
  if (!grid) return;

  const filtered = filter === "all" 
    ? PROJECTS_DATA 
    : PROJECTS_DATA.filter(item => item.category === filter);

  grid.innerHTML = filtered.map((proj, idx) => {
    return `
      <div class="gallery-card t3d rv in" data-id="${proj.id}" onclick="openProjectModal('${proj.id}')" style="transition-delay:${idx * 0.05}s">
        <div class="g-visual-wrap">
          ${getSvgVisual(proj.svgIcon, proj.title)}
          <div class="g-overlay">
            <span class="g-type-badge">${proj.type}</span>
            <span class="g-zoom">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
              View
            </span>
          </div>
        </div>
        <div class="g-body">
          <h3 class="g-title">${proj.title}</h3>
          <p class="g-desc">${proj.shortDesc}</p>
          <div class="g-tags">
            ${proj.tags.map(t => `<span class="g-tag">${t}</span>`).join('')}
          </div>
          <div class="g-actions" onclick="event.stopPropagation()">
            <button class="btn-preview" onclick="openProjectModal('${proj.id}')">
              <span>Explore Details</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </button>
            <a href="${proj.link}" target="_blank" rel="noopener noreferrer" class="btn-linkedin" title="Open LinkedIn Post">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
              <span>Post ↗</span>
            </a>
          </div>
        </div>
      </div>
    `;
  }).join('');

  // Re-bind tilt physics on new cards
  bindTiltPhysics();
}

// Lightbox Modal Logic
function openProjectModal(id) {
  const proj = PROJECTS_DATA.find(p => p.id === id);
  if (!proj) return;

  const lb = document.getElementById("lb");
  const lbTtl = document.getElementById("lb-ttl");
  const lbBanner = document.getElementById("lb-banner");
  const lbBadge = document.getElementById("lb-badge");
  const lbDesc = document.getElementById("lb-desc");
  const lbHighlights = document.getElementById("lb-highlights");
  const lbLink = document.getElementById("lb-link");

  lbTtl.textContent = proj.title;
  lbBanner.innerHTML = getSvgVisual(proj.svgIcon, proj.title);
  lbBadge.textContent = proj.type;
  lbDesc.textContent = proj.fullDesc;
  
  lbHighlights.innerHTML = proj.highlights.map(h => `
    <li>
      <div class="bdot" style="background:var(--accent);"></div>
      <span>${h}</span>
    </li>
  `).join('');

  lbLink.href = proj.link;

  lb.classList.add("on");
  document.body.style.overflow = "hidden";
}

function lbOff() {
  const lb = document.getElementById("lb");
  if (lb) lb.classList.remove("on");
  document.body.style.overflow = "";
}

function lbClose(e) {
  if (e.target === document.getElementById("lb")) {
    lbOff();
  }
}

// Global escape key listener
document.addEventListener("keydown", e => {
  if (e.key === "Escape") lbOff();
});

// Category Filter Click Handler
function setupFilterTabs() {
  const buttons = document.querySelectorAll(".filter-btn");
  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      buttons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const cat = btn.dataset.cat;
      renderProjects(cat);
    });
  });
}

// Counter Animation for Stats
function animateCounters() {
  const counters = document.querySelectorAll("[data-target]");
  const counterObs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.target, 10);
        let cur = 0;
        const step = Math.max(1, target / 40);
        const timer = setInterval(() => {
          cur += step;
          if (cur >= target) {
            el.textContent = target + "+";
            clearInterval(timer);
            return;
          }
          el.textContent = Math.floor(cur) + "+";
        }, 30);
        counterObs.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(el => counterObs.observe(el));
}

// Scroll Reveal with IntersectionObserver
function setupScrollReveal() {
  const rvEls = document.querySelectorAll(".rv");
  const rvObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add("in");
      }
    });
  }, { threshold: 0.08 });

  rvEls.forEach(el => rvObs.observe(el));
}

// 3D Tilt Physics Engine
function bindTiltPhysics() {
  const isTouch = window.matchMedia("(pointer: coarse)").matches;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (isTouch || reduceMotion) return;

  const tiltTargets = document.querySelectorAll(".stat-c, .gallery-card, .about-card, .edu, .sk-cat-card, .ec");
  
  tiltTargets.forEach(el => {
    let raf = null;
    el.addEventListener("mousemove", e => {
      const rect = el.getBoundingClientRect();
      const px = (e.clientX - rect.left) / rect.width - 0.5;
      const py = (e.clientY - rect.top) / rect.height - 0.5;
      
      if (raf) cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const rx = (-py * 12).toFixed(2);
        const ry = (px * 12).toFixed(2);
        el.style.transform = `translateY(-8px) translateZ(24px) rotateX(${rx}deg) rotateY(${ry}deg)`;
      });
    });

    el.addEventListener("mouseleave", () => {
      if (raf) cancelAnimationFrame(raf);
      el.style.transform = "";
    });
  });
}

// Cursor Spotlight Glow
function setupCursorGlow() {
  const isTouch = window.matchMedia("(pointer: coarse)").matches;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (isTouch || reduceMotion) return;

  const glow = document.createElement("div");
  glow.className = "cursor-glow";
  glow.style.opacity = "0";
  document.body.appendChild(glow);

  let tx = 0, ty = 0, cx = 0, cy = 0, raf = null;

  function update() {
    cx += (tx - cx) * 0.14;
    cy += (ty - cy) * 0.14;
    glow.style.transform = `translate(${cx}px, ${cy}px) translate(-50%, -50%)`;
    raf = requestAnimationFrame(update);
  }

  document.addEventListener("mousemove", e => {
    tx = e.clientX;
    ty = e.clientY;
    glow.style.opacity = "1";
    if (!raf) raf = requestAnimationFrame(update);
  });

  document.addEventListener("mouseleave", () => {
    glow.style.opacity = "0";
  });
}

// Theme Switcher (Dark / Light)
function setupThemeToggle() {
  const toggleBtn = document.getElementById("theme-toggle");
  if (!toggleBtn) return;

  const savedTheme = localStorage.getItem("amit_portfolio_theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const currentTheme = savedTheme || (prefersDark ? "dark" : "light");

  document.documentElement.setAttribute("data-theme", currentTheme);
  updateThemeIcon(currentTheme);

  toggleBtn.addEventListener("click", () => {
    const active = document.documentElement.getAttribute("data-theme");
    const nextTheme = active === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", nextTheme);
    localStorage.setItem("amit_portfolio_theme", nextTheme);
    updateThemeIcon(nextTheme);
  });
}

function updateThemeIcon(theme) {
  const icon = document.getElementById("theme-icon");
  if (!icon) return;
  if (theme === "dark") {
    // Sun icon for switching to light
    icon.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`;
  } else {
    // Moon icon for switching to dark
    icon.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
  }
}

// Mobile Menu Navigation
function setupMobileMenu() {
  const btn = document.getElementById("mobile-menu-btn");
  const drawer = document.getElementById("mobile-drawer");
  if (!btn || !drawer) return;

  btn.addEventListener("click", () => {
    drawer.classList.toggle("open");
  });

  drawer.querySelectorAll("a").forEach(a => {
    a.addEventListener("click", () => {
      drawer.classList.remove("open");
    });
  });
}

// Initialization on DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
  setupThemeToggle();
  setupMobileMenu();
  renderProjects("all");
  setupFilterTabs();
  animateCounters();
  setupScrollReveal();
  bindTiltPhysics();
  setupCursorGlow();
});
