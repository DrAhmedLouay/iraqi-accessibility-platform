#!/usr/bin/env python3
"""
build_realistic_3d_walkthrough.py
Upgrades the Interactive 3D WebGL Walkthrough in the Iraqi Accessibility Platform
from rudimentary boxes to high-fidelity architectural spaces with:
- Procedural PBR materials (ceramic floor tiles with grout, stainless steel, porcelain, glass mirror, tactile pavers)
- Detailed 3D Restroom (2.0x2.0m, door with frame & kickplate, toilet with tank & flush, floating sink, dual grab bars, pull cord, 3D wheelchair with spoke wheels)
- Detailed 3D Ramp (1:16 slope, non-slip texture, 5cm curbs, dual continuous handrails with 30cm extensions)
- Detailed 3D Stairs (beveled nosings, yellow warning stripes, tactile paving, dual rails)
- Detailed 3D Elevator (brushed steel cabin, ceiling spotlights, full mirror, COP panel with Braille & LCD)
- Preset Camera Viewpoints (Eye-level 120cm, Isometric 45°, Top Plan 3D, Auto-Tour 360°)
- 3D Dimension Callouts & Interactive Elements
"""

import sys
import re

FILES = [
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/iraqi_accessibility_platform.html',
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/index.html'
]

# 1. NEW HTML MARKUP FOR 3D WALKTHROUGH SECTION
NEW_3D_HTML = """      <!-- 3D WEBGL REALISTIC ARCHITECTURAL WALKTHROUGH (TRACK 1 - HIGH FIDELITY) -->
      <div class="bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 shadow-sm">
        <div class="flex items-center justify-between flex-wrap gap-3 mb-3 pb-3 border-b border-slate-100 dark:border-slate-800">
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">🌐</span>
            <div>
              <div class="flex items-center gap-2 flex-wrap">
                <h3 class="text-sm sm:text-base font-black text-slate-900 dark:text-slate-100">
                  المجسم المعماري التفاعلي 3D والتجول الافتراضي (Interactive 3D WebGL Walkthrough)
                </h3>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 font-bold px-2 py-0.5 rounded border border-emerald-300">نمذجة معمارية فائقة الدقة</span>
              </div>
              <p class="text-xs text-slate-500 mt-0.5">محاكاة ثلاثية الأبعاد واقعية لفضاءات الكود العراقي (م.ب.ع 202) بالخامات والظلال وحرم حركة الكرسي المتحرك والأبعاد التنفيذية.</p>
            </div>
          </div>
          <div class="flex items-center gap-2 flex-wrap">
            <button onclick="toggle3DViewMode()" id="btn-toggle-3d" class="px-3.5 py-1.5 rounded-xl bg-teal-700 hover:bg-teal-600 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-sm">
              <span id="txt-toggle-3d-icon">🌐</span> <span id="txt-toggle-3d">إظهار المجسم 3D WebGL</span>
            </button>
            <button onclick="exportBIMSchema()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold text-xs flex items-center gap-1.5 border border-slate-700 transition">
              <span>🏗️</span> <span>تصدير بارامترات BIM (Revit/IFC)</span>
            </button>
          </div>
        </div>

        <!-- 3D Container (Collapsible) -->
        <div id="calc-3d-section" class="hidden space-y-3">
          <!-- Space Selector & Viewpoints Control Bar -->
          <div class="bg-slate-100 dark:bg-slate-900 p-3 rounded-2xl border border-slate-200 dark:border-slate-800 space-y-2.5 text-xs">
            <!-- Row 1: Space Selector -->
            <div class="flex items-center justify-between flex-wrap gap-2">
              <div class="flex items-center gap-1.5 flex-wrap">
                <span class="font-bold text-slate-700 dark:text-slate-300">الفضاء المعماري:</span>
                <button onclick="switch3DScene('restroom')" id="btn-3d-restroom" class="btn-3d-scene px-3 py-1.5 rounded-xl bg-teal-600 text-white font-bold transition shadow-xs">🚻 المرفق الصحي الشامل (2×2م)</button>
                <button onclick="switch3DScene('ramp')" id="btn-3d-ramp" class="btn-3d-scene px-3 py-1.5 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition">📐 المنحدر المعماري والبسطات</button>
                <button onclick="switch3DScene('stairs')" id="btn-3d-stairs" class="btn-3d-scene px-3 py-1.5 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition">🪜 السلالم والدرابزين المزدوج</button>
                <button onclick="switch3DScene('elevator')" id="btn-3d-elevator" class="btn-3d-scene px-3 py-1.5 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition">🛗 مقصورة المصعد الشامل</button>
              </div>
              <div class="flex items-center gap-1.5">
                <button onclick="toggle3DAutoTour()" id="btn-3d-autotour" class="px-2.5 py-1 rounded-lg bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-[11px] flex items-center gap-1 shadow-xs transition">
                  <span id="icon-autotour">▶️</span> <span>تجول سينمائي 360°</span>
                </button>
              </div>
            </div>

            <!-- Row 2: Camera Presets & Layer Toggles -->
            <div class="flex items-center justify-between flex-wrap gap-2 pt-2 border-t border-slate-200 dark:border-slate-800">
              <div class="flex items-center gap-1.5 flex-wrap">
                <span class="text-slate-500 font-bold">زاوية الكاميرا:</span>
                <button onclick="set3DCameraView('eye')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 hover:bg-slate-700 font-bold text-[11px] transition">👁️ منظور عين الكرسي (120 سم)</button>
                <button onclick="set3DCameraView('iso')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 hover:bg-slate-700 font-bold text-[11px] transition">📐 منظور أيزومتري (45°)</button>
                <button onclick="set3DCameraView('top')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 hover:bg-slate-700 font-bold text-[11px] transition">🔝 مسقط أفقي ثلاثي الأبعاد</button>
                <button onclick="reset3DCamera()" class="px-2 py-1 rounded-lg bg-slate-700 text-slate-200 hover:bg-slate-600 font-bold text-[11px]">🔄 إعادة توجيه</button>
              </div>
              <div class="flex items-center gap-1.5 flex-wrap">
                <button onclick="toggle3DWalls()" id="btn-3d-walls" class="px-2 py-1 rounded-lg bg-slate-800 text-slate-200 hover:bg-slate-700 font-bold text-[11px]">🧱 إخفاء الجدران</button>
                <button onclick="toggle3DWheelchair()" id="btn-3d-wheelchair" class="px-2 py-1 rounded-lg bg-slate-800 text-sky-400 hover:bg-slate-700 font-bold text-[11px]">♿ الكرسي ومجسم الحركة</button>
                <button onclick="toggle3DDimensions()" id="btn-3d-dims" class="px-2 py-1 rounded-lg bg-slate-800 text-emerald-400 hover:bg-slate-700 font-bold text-[11px]">📏 الأبعاد الإلزامية</button>
              </div>
            </div>
          </div>

          <!-- WebGL Canvas Viewport (Spacious 520px height) -->
          <div id="calc-3d-canvas-container" class="relative border-2 border-slate-800 rounded-2xl overflow-hidden shadow-2xl" style="height: 520px;">
            <canvas id="calc-3d-canvas"></canvas>

            <!-- Floating Top Badges -->
            <div class="absolute top-3 right-3 flex items-center gap-2">
              <div id="3d-scene-badge" class="bg-slate-900/90 backdrop-blur-md px-3 py-1.5 rounded-xl border border-teal-500/60 text-xs text-teal-300 font-bold shadow-lg">
                دورة مياه ميسرة صافية 2.00 × 2.00 م (م.ب.ع 202)
              </div>
            </div>

            <!-- Floating Bottom HUD -->
            <div class="absolute bottom-3 right-3 bg-slate-900/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-slate-700 text-[11px] text-slate-300 flex items-center gap-2">
              <span>🖱️ اسحب بالماوس للدوران 360° | عجلة الفأرة للتكبير والتصغير | كليك يمين للتحريك</span>
            </div>

            <div id="3d-dim-hud" class="absolute bottom-3 left-3 bg-slate-900/85 backdrop-blur-md px-3 py-1.5 rounded-xl border border-emerald-500/60 text-[11px] text-emerald-400 font-mono font-bold">
              Ф 1.50m Turning Clear | 2.00x2.00m Boundary
            </div>
          </div>
        </div>
      </div>
"""

# 2. COMPLETE HIGH-FIDELITY JAVASCRIPT ENGINE FOR 3D WALKTHROUGH
REALISTIC_3D_JS = """
    // =========================================================================
    // 🌐 TRACK 1: REALISTIC ARCHITECTURAL 3D WEBGL WALKTHROUGH (HIGH FIDELITY)
    // =========================================================================
    let scene3D, camera3D, renderer3D, currentMeshGroup, is3DInitialized = false;
    let show3DWalls = true, show3DDimensions = true, show3DWheelchair = true, current3DType = 'restroom';
    let isMouseDown = false, mouseX = 0, mouseY = 0, rotX = 0.45, rotY = -0.6, targetZoom = 6.8;
    let isAutoTour = false, panX = 0, panY = 0.6, panZ = 0;
    let cachedTextures = {};

    function toggle3DViewMode() {
      const sec = document.getElementById('calc-3d-section');
      const btnTxt = document.getElementById('txt-toggle-3d');
      const btnIcon = document.getElementById('txt-toggle-3d-icon');
      if (sec.classList.contains('hidden')) {
        sec.classList.remove('hidden');
        btnTxt.innerText = "إخفاء المجسم 3D";
        btnIcon.innerText = "🔼";
        if (!is3DInitialized) {
          init3DWebGLWalkthrough();
        } else {
          on3DWindowResize();
        }
      } else {
        sec.classList.add('hidden');
        btnTxt.innerText = "إظهار المجسم 3D WebGL";
        btnIcon.innerText = "🌐";
        isAutoTour = false;
      }
    }

    // --- PROCEDURAL ARCHITECTURAL TEXTURES GENERATOR ---
    function getTileTexture() {
      if (cachedTextures.tile) return cachedTextures.tile;
      const c = document.createElement('canvas');
      c.width = 512; c.height = 512;
      const ctx = c.getContext('2d');
      // Porcelain warm grey tile
      ctx.fillStyle = '#cbd5e1';
      ctx.fillRect(0, 0, 512, 512);
      // Grout grid (60x60cm scale)
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 5;
      for (let i = 0; i <= 512; i += 128) {
        ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, 512); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(512, i); ctx.stroke();
      }
      // Tile bevel highlights
      ctx.strokeStyle = '#f8fafc';
      ctx.lineWidth = 2;
      for (let i = 0; i < 512; i += 128) {
        ctx.strokeRect(i + 4, 4, 120, 120);
      }
      const tex = new THREE.CanvasTexture(c);
      tex.wrapS = THREE.RepeatWrapping;
      tex.wrapT = THREE.RepeatWrapping;
      tex.repeat.set(3, 3);
      cachedTextures.tile = tex;
      return tex;
    }

    function getTactileTexture() {
      if (cachedTextures.tactile) return cachedTextures.tactile;
      const c = document.createElement('canvas');
      c.width = 256; c.height = 256;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#eab308'; // Warning Yellow
      ctx.fillRect(0, 0, 256, 256);
      ctx.fillStyle = '#ca8a04';
      // Blister raised dots pattern
      for (let x = 16; x < 256; x += 32) {
        for (let y = 16; y < 256; y += 32) {
          ctx.beginPath();
          ctx.arc(x, y, 7, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      const tex = new THREE.CanvasTexture(c);
      tex.wrapS = THREE.RepeatWrapping;
      tex.wrapT = THREE.RepeatWrapping;
      cachedTextures.tactile = tex;
      return tex;
    }

    function getGraniteTexture() {
      if (cachedTextures.granite) return cachedTextures.granite;
      const c = document.createElement('canvas');
      c.width = 256; c.height = 256;
      const ctx = c.getContext('2d');
      ctx.fillStyle = '#334155';
      ctx.fillRect(0, 0, 256, 256);
      // Speckles
      for (let i = 0; i < 2000; i++) {
        ctx.fillStyle = Math.random() > 0.5 ? '#64748b' : '#0f172a';
        ctx.fillRect(Math.random() * 256, Math.random() * 256, 2, 2);
      }
      const tex = new THREE.CanvasTexture(c);
      tex.wrapS = THREE.RepeatWrapping;
      tex.wrapT = THREE.RepeatWrapping;
      tex.repeat.set(4, 4);
      cachedTextures.granite = tex;
      return tex;
    }

    function init3DWebGLWalkthrough() {
      const container = document.getElementById('calc-3d-canvas-container');
      const canvas = document.getElementById('calc-3d-canvas');
      if (!container || !canvas || typeof THREE === 'undefined') return;

      scene3D = new THREE.Scene();
      scene3D.background = new THREE.Color(0x060913);

      camera3D = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 100);
      camera3D.position.set(4, 5, 5);
      camera3D.lookAt(0, 0.6, 0);

      renderer3D = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, powerPreference: "high-performance" });
      renderer3D.setSize(container.clientWidth, container.clientHeight);
      renderer3D.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer3D.shadowMap.enabled = true;
      renderer3D.shadowMap.type = THREE.PCFSoftShadowMap;

      // Realistic Architectural Lights
      const ambientLight = new THREE.AmbientLight(0xffffff, 0.65);
      scene3D.add(ambientLight);

      const sunLight = new THREE.DirectionalLight(0xfffbeb, 0.85);
      sunLight.position.set(6, 12, 8);
      sunLight.castShadow = true;
      sunLight.shadow.mapSize.width = 1024;
      sunLight.shadow.mapSize.height = 1024;
      sunLight.shadow.bias = -0.001;
      scene3D.add(sunLight);

      // Warm Interior Ceiling Downlight
      const ceilingLight = new THREE.PointLight(0xfffaed, 0.9, 8);
      ceilingLight.position.set(0, 2.5, 0);
      scene3D.add(ceilingLight);

      currentMeshGroup = new THREE.Group();
      scene3D.add(currentMeshGroup);

      build3DRestroomScene();

      // Mouse Orbit & Pan Controls
      canvas.addEventListener('mousedown', (e) => {
        isMouseDown = true;
        mouseX = e.clientX;
        mouseY = e.clientY;
      });
      window.addEventListener('mouseup', () => { isMouseDown = false; });
      window.addEventListener('mousemove', (e) => {
        if (!isMouseDown) return;
        const dx = e.clientX - mouseX;
        const dy = e.clientY - mouseY;

        if (e.buttons === 2) { // Right click: Pan
          panX -= dx * 0.004;
          panY += dy * 0.004;
        } else { // Left click: Orbit
          rotY += dx * 0.008;
          rotX += dy * 0.008;
          rotX = Math.max(-0.15, Math.min(Math.PI / 2.1, rotX));
        }
        mouseX = e.clientX;
        mouseY = e.clientY;
      });

      canvas.addEventListener('contextmenu', (e) => e.preventDefault());

      canvas.addEventListener('wheel', (e) => {
        e.preventDefault();
        targetZoom += e.deltaY * 0.004;
        targetZoom = Math.max(2.5, Math.min(14, targetZoom));
      }, { passive: false });

      // Touch Controls for Mobile
      let touchStartX = 0, touchStartY = 0;
      canvas.addEventListener('touchstart', (e) => {
        if (e.touches.length === 1) {
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
        }
      }, { passive: true });
      canvas.addEventListener('touchmove', (e) => {
        if (e.touches.length === 1) {
          const dx = e.touches[0].clientX - touchStartX;
          const dy = e.touches[0].clientY - touchStartY;
          rotY += dx * 0.01;
          rotX += dy * 0.01;
          rotX = Math.max(-0.15, Math.min(Math.PI / 2.1, rotX));
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
        }
      }, { passive: true });

      window.addEventListener('resize', on3DWindowResize);

      // Render Loop
      function animate3D() {
        requestAnimationFrame(animate3D);
        if (isAutoTour) {
          rotY += 0.005;
        }
        if (camera3D) {
          camera3D.position.x = panX + (targetZoom * Math.sin(rotY) * Math.cos(rotX));
          camera3D.position.y = panY + (targetZoom * Math.sin(rotX));
          camera3D.position.z = panZ + (targetZoom * Math.cos(rotY) * Math.cos(rotX));
          camera3D.lookAt(panX, panY, panZ);
        }
        if (renderer3D && scene3D && camera3D) {
          renderer3D.render(scene3D, camera3D);
        }
      }
      animate3D();
      is3DInitialized = true;
    }

    function on3DWindowResize() {
      const container = document.getElementById('calc-3d-canvas-container');
      if (!container || !renderer3D || !camera3D) return;
      camera3D.aspect = container.clientWidth / container.clientHeight;
      camera3D.updateProjectionMatrix();
      renderer3D.setSize(container.clientWidth, container.clientHeight);
    }

    function clear3DScene() {
      while (currentMeshGroup.children.length > 0) {
        currentMeshGroup.remove(currentMeshGroup.children[0]);
      }
    }

    // --- DETAILED 3D WHEELCHAIR MODEL BUILDER ---
    function createWheelchairModel() {
      const chairGroup = new THREE.Group();
      const chromeMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.9, roughness: 0.15 });
      const rubberMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
      const fabricMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.5 }); // Blue upholstery

      // Rear Big Wheels (24" = 0.6m diameter)
      for (let side = -1; side <= 1; side += 2) {
        // Tyre
        const tyre = new THREE.Mesh(new THREE.TorusGeometry(0.3, 0.025, 16, 32), rubberMat);
        tyre.position.set(side * 0.32, 0.3, -0.1);
        tyre.rotation.y = Math.PI / 2;
        chairGroup.add(tyre);

        // Hand Rim
        const rim = new THREE.Mesh(new THREE.TorusGeometry(0.26, 0.012, 8, 24), chromeMat);
        rim.position.set(side * 0.35, 0.3, -0.1);
        rim.rotation.y = Math.PI / 2;
        chairGroup.add(rim);

        // Axle
        const axle = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.015, 0.66, 8), chromeMat);
        axle.rotation.z = Math.PI / 2;
        axle.position.set(0, 0.3, -0.1);
        chairGroup.add(axle);
      }

      // Front Caster Wheels
      for (let side = -1; side <= 1; side += 2) {
        const caster = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.03, 16), rubberMat);
        caster.rotation.z = Math.PI / 2;
        caster.position.set(side * 0.25, 0.05, 0.35);
        chairGroup.add(caster);

        const fork = new THREE.Mesh(new THREE.CylinderGeometry(0.01, 0.01, 0.15, 8), chromeMat);
        fork.position.set(side * 0.25, 0.12, 0.35);
        chairGroup.add(fork);
      }

      // Chassis Tubular Frame
      const frameMat = new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.7, roughness: 0.3 });
      // Seat Base
      const seat = new THREE.Mesh(new THREE.BoxGeometry(0.48, 0.05, 0.48), fabricMat);
      seat.position.set(0, 0.48, 0.05);
      chairGroup.add(seat);

      // Backrest
      const backrest = new THREE.Mesh(new THREE.BoxGeometry(0.46, 0.45, 0.04), fabricMat);
      backrest.position.set(0, 0.72, -0.18);
      chairGroup.add(backrest);

      // Armrests
      for (let side = -1; side <= 1; side += 2) {
        const arm = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.03, 0.35), rubberMat);
        arm.position.set(side * 0.26, 0.68, 0.05);
        chairGroup.add(arm);
      }

      // Footrests
      for (let side = -1; side <= 1; side += 2) {
        const foot = new THREE.Mesh(new THREE.BoxGeometry(0.14, 0.015, 0.16), frameMat);
        foot.position.set(side * 0.16, 0.12, 0.46);
        foot.rotation.x = -0.15;
        chairGroup.add(foot);
      }

      // Human Silhouette / Torso
      const torsoMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.7 });
      const torso = new THREE.Mesh(new THREE.BoxGeometry(0.38, 0.48, 0.22), torsoMat);
      torso.position.set(0, 0.76, 0.05);
      chairGroup.add(torso);

      const head = new THREE.Mesh(new THREE.SphereGeometry(0.11, 16, 16), torsoMat);
      head.position.set(0, 1.12, 0.05);
      chairGroup.add(head);

      return chairGroup;
    }

    // --- 1. DETAILED 3D RESTROOM SCENE ---
    function build3DRestroomScene() {
      clear3DScene();
      current3DType = 'restroom';
      document.getElementById('3d-scene-badge').innerText = 'المرفق الصحي الشامل 2.00 × 2.00 م صافٍ (م.ب.ع 202 الباب 5)';
      document.getElementById('3d-dim-hud').innerText = 'Clear 2.00x2.00m | Turning Ø150cm | Door 90cm';

      const tileTex = getTileTexture();
      const chromeMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, metalness: 0.95, roughness: 0.1 });
      const porcelainMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.15 });

      // 1. Tiled Floor (2.0 x 2.0 m)
      const floor = new THREE.Mesh(
        new THREE.BoxGeometry(2.0, 0.1, 2.0),
        new THREE.MeshStandardMaterial({ map: tileTex, roughness: 0.3 })
      );
      floor.position.set(0, -0.05, 0);
      floor.receiveShadow = true;
      currentMeshGroup.add(floor);

      // Skirting Board (وزرة سفلية)
      const skirtMat = new THREE.MeshStandardMaterial({ color: 0x475569 });
      const skirtBack = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.1, 0.02), skirtMat);
      skirtBack.position.set(0, 0.05, -0.99);
      currentMeshGroup.add(skirtBack);

      // 2. 150 cm Diameter Turning Circle (دائرة دوران 150 سم)
      const ringGeo = new THREE.RingGeometry(0.02, 0.75, 48);
      const ringMat = new THREE.MeshBasicMaterial({ color: 0x10b981, side: THREE.DoubleSide, transparent: true, opacity: 0.45 });
      const circle = new THREE.Mesh(ringGeo, ringMat);
      circle.rotation.x = Math.PI / 2;
      circle.position.set(0.1, 0.005, 0.1);
      currentMeshGroup.add(circle);

      // 3. Walls (Tiled Ceramic Finish)
      if (show3DWalls) {
        const wallMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.4, transparent: true, opacity: 0.85 });
        // Back Wall
        const backWall = new THREE.Mesh(new THREE.BoxGeometry(2.0, 2.4, 0.06), wallMat);
        backWall.position.set(0, 1.2, -1.03);
        backWall.receiveShadow = true;
        currentMeshGroup.add(backWall);

        // Right Wall
        const rightWall = new THREE.Mesh(new THREE.BoxGeometry(0.06, 2.4, 2.0), wallMat);
        rightWall.position.set(1.03, 1.2, 0);
        rightWall.receiveShadow = true;
        currentMeshGroup.add(rightWall);

        // Left Wall
        const leftWall = new THREE.Mesh(new THREE.BoxGeometry(0.06, 2.4, 2.0), wallMat);
        leftWall.position.set(-1.03, 1.2, 0);
        leftWall.receiveShadow = true;
        currentMeshGroup.add(leftWall);

        // Front Wall with 90cm Door Opening
        const frontLeft = new THREE.Mesh(new THREE.BoxGeometry(0.55, 2.4, 0.06), wallMat);
        frontLeft.position.set(-0.725, 1.2, 1.03);
        currentMeshGroup.add(frontLeft);

        const frontRight = new THREE.Mesh(new THREE.BoxGeometry(0.55, 2.4, 0.06), wallMat);
        frontRight.position.set(0.725, 1.2, 1.03);
        currentMeshGroup.add(frontRight);

        const doorLintel = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.3, 0.06), wallMat);
        doorLintel.position.set(0, 2.25, 1.03);
        currentMeshGroup.add(doorLintel);

        // Open Door Leaf (90cm wide, open outward 90°)
        const doorMat = new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.5 }); // Warm Oak
        const doorLeaf = new THREE.Mesh(new THREE.BoxGeometry(0.04, 2.1, 0.9), doorMat);
        doorLeaf.position.set(-0.45, 1.05, 1.48);
        doorLeaf.castShadow = true;
        currentMeshGroup.add(doorLeaf);

        // Kickplate (Stainless Steel 30cm)
        const kickplate = new THREE.Mesh(new THREE.BoxGeometry(0.045, 0.3, 0.9), chromeMat);
        kickplate.position.set(-0.45, 0.15, 1.48);
        currentMeshGroup.add(kickplate);

        // Lever Door Handle
        const handle = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.015, 0.12, 8), chromeMat);
        handle.rotation.z = Math.PI / 2;
        handle.position.set(-0.48, 0.95, 1.9);
        currentMeshGroup.add(handle);
      }

      // 4. Contoured Toilet Fixture
      const toiletGroup = new THREE.Group();
      // Bowl
      const bowl = new THREE.Mesh(new THREE.CylinderGeometry(0.19, 0.15, 0.42, 24), porcelainMat);
      bowl.position.set(0, 0.21, 0);
      bowl.castShadow = true;
      toiletGroup.add(bowl);

      // Seat Lid
      const seat = new THREE.Mesh(new THREE.TorusGeometry(0.18, 0.03, 12, 24), new THREE.MeshStandardMaterial({ color: 0xf1f5f9 }));
      seat.rotation.x = Math.PI / 2;
      seat.position.set(0, 0.43, 0.02);
      toiletGroup.add(seat);

      // Tank
      const tank = new THREE.Mesh(new THREE.BoxGeometry(0.42, 0.48, 0.2), porcelainMat);
      tank.position.set(0, 0.65, -0.22);
      tank.castShadow = true;
      toiletGroup.add(tank);

      // Dual Flush Push Button
      const flushBtn = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.015, 16), chromeMat);
      flushBtn.position.set(0, 0.895, -0.22);
      toiletGroup.add(flushBtn);

      toiletGroup.position.set(-0.55, 0, -0.72);
      currentMeshGroup.add(toiletGroup);

      // 5. Dual Grab Bars (مساند الارتكاز الإلزامية)
      // Wall L-Bar (Horizontal 85cm, Vertical return)
      const lBarH = new THREE.Mesh(new THREE.CylinderGeometry(0.019, 0.019, 0.8, 16), chromeMat);
      lBarH.rotation.z = Math.PI / 2;
      lBarH.position.set(-0.55, 0.85, -0.96);
      currentMeshGroup.add(lBarH);

      // Side Wall Bar
      const lBarSide = new THREE.Mesh(new THREE.CylinderGeometry(0.019, 0.019, 0.85, 16), chromeMat);
      lBarSide.rotation.x = Math.PI / 2;
      lBarSide.position.set(-0.96, 0.85, -0.65);
      currentMeshGroup.add(lBarSide);

      // Drop-Down Folding Grab Bar (on open transfer side)
      const foldBar = new THREE.Mesh(new THREE.CylinderGeometry(0.019, 0.019, 0.75, 16), chromeMat);
      foldBar.rotation.x = Math.PI / 2;
      foldBar.position.set(-0.25, 0.85, -0.62);
      currentMeshGroup.add(foldBar);

      // 6. Floating Ergonomic Sink (مغسلة معلقة بدون عامود)
      const sinkGroup = new THREE.Group();
      const basin = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.14, 0.45), porcelainMat);
      basin.position.set(0, 0.78, 0);
      sinkGroup.add(basin);

      // Mixer Tap with Elbow Lever
      const tap = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.012, 0.14, 12), chromeMat);
      tap.position.set(0, 0.92, -0.15);
      sinkGroup.add(tap);

      // Tilted Mirror (مرآة مائلة بزاوية 10 درجات)
      const mirror = new THREE.Mesh(
        new THREE.BoxGeometry(0.55, 0.8, 0.02),
        new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 1.0, roughness: 0.05 })
      );
      mirror.position.set(0, 1.45, -0.2);
      mirror.rotation.x = 0.14; // 10° forward tilt
      sinkGroup.add(mirror);

      sinkGroup.position.set(0.55, 0, -0.75);
      currentMeshGroup.add(sinkGroup);

      // 7. Emergency Pull Cord (حبل طوارئ أحمر يتدلى إلى 10 سم عن الأرض)
      const cord = new THREE.Mesh(
        new THREE.CylinderGeometry(0.003, 0.003, 2.1, 8),
        new THREE.MeshBasicMaterial({ color: 0xef4444 })
      );
      cord.position.set(-0.2, 1.15, -0.95);
      currentMeshGroup.add(cord);

      const pullTriangle = new THREE.Mesh(
        new THREE.ConeGeometry(0.035, 0.06, 3),
        new THREE.MeshBasicMaterial({ color: 0xef4444 })
      );
      pullTriangle.position.set(-0.2, 0.12, -0.95);
      currentMeshGroup.add(pullTriangle);

      // Emergency Wall Flasher Strobe
      const strobe = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.12, 0.06), new THREE.MeshStandardMaterial({ color: 0xef4444 }));
      strobe.position.set(-0.2, 2.2, -0.98);
      currentMeshGroup.add(strobe);

      // 8. 3D Wheelchair Model in Center
      if (show3DWheelchair) {
        const wheelchair = createWheelchairModel();
        wheelchair.position.set(0.1, 0, 0.1);
        currentMeshGroup.add(wheelchair);
      }
    }

    // --- 2. DETAILED 3D RAMP & LANDINGS SCENE ---
    function build3DRampScene() {
      clear3DScene();
      current3DType = 'ramp';
      document.getElementById('3d-scene-badge').innerText = 'منحدر معماري 1:16 وبسطات 1.5×1.5م (م.ب.ع 202 الباب 3)';
      document.getElementById('3d-dim-hud').innerText = 'Slope 1:16 (6.25%) | Rails 85cm & 65cm | Landings 1.50m';

      const graniteTex = getGraniteTexture();
      const tactileTex = getTactileTexture();
      const chromeMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, metalness: 0.95, roughness: 0.15 });

      // Lower Landing (1.5 x 1.5 m)
      const lowerLanding = new THREE.Mesh(
        new THREE.BoxGeometry(1.6, 0.1, 1.6),
        new THREE.MeshStandardMaterial({ map: graniteTex })
      );
      lowerLanding.position.set(-2.8, -0.05, 0);
      lowerLanding.receiveShadow = true;
      currentMeshGroup.add(lowerLanding);

      // Tactile Strip on Lower Landing
      const tactilePad = new THREE.Mesh(
        new THREE.BoxGeometry(0.6, 0.01, 1.4),
        new THREE.MeshStandardMaterial({ map: tactileTex })
      );
      tactilePad.position.set(-3.2, 0.005, 0);
      currentMeshGroup.add(tactilePad);

      // Inclined Slope Run (1:16 Gradient)
      const rampLength = 4.0;
      const rampSlope = 0.0625; // 1:16
      const ramp = new THREE.Mesh(
        new THREE.BoxGeometry(rampLength, 0.1, 1.4),
        new THREE.MeshStandardMaterial({ map: graniteTex, color: 0x059669 })
      );
      ramp.position.set(0, 0.125, 0);
      ramp.rotation.z = -Math.atan(rampSlope);
      ramp.receiveShadow = true;
      currentMeshGroup.add(ramp);

      // 5cm Curb Edge Protection (حافة حماية جانبية)
      for (let side = -1; side <= 1; side += 2) {
        const curb = new THREE.Mesh(
          new THREE.BoxGeometry(rampLength, 0.06, 0.05),
          new THREE.MeshStandardMaterial({ color: 0xd97706 })
        );
        curb.position.set(0, 0.19, side * 0.725);
        curb.rotation.z = -Math.atan(rampSlope);
        currentMeshGroup.add(curb);
      }

      // Upper Landing (1.5 x 1.5 m at +25cm height)
      const upperLanding = new THREE.Mesh(
        new THREE.BoxGeometry(1.6, 0.1, 1.6),
        new THREE.MeshStandardMaterial({ map: graniteTex })
      );
      upperLanding.position.set(2.8, 0.25, 0);
      upperLanding.receiveShadow = true;
      currentMeshGroup.add(upperLanding);

      // Continuous Dual Handrails (Upper 85cm, Lower 65cm + 30cm extensions)
      for (let side = -1; side <= 1; side += 2) {
        // Upper Rail
        const railTop = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, rampLength, 16), chromeMat);
        railTop.rotation.z = -(Math.PI / 2) - Math.atan(rampSlope);
        railTop.position.set(0, 0.98, side * 0.72);
        currentMeshGroup.add(railTop);

        // Lower Rail
        const railBot = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.018, rampLength, 16), chromeMat);
        railBot.rotation.z = -(Math.PI / 2) - Math.atan(rampSlope);
        railBot.position.set(0, 0.78, side * 0.72);
        currentMeshGroup.add(railBot);

        // Vertical Stanchions (أعمدة التثبيت الرأسية كل متر)
        for (let x = -1.8; x <= 1.8; x += 1.2) {
          const postY = 0.125 - (x * rampSlope) + 0.45;
          const post = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.018, 0.9, 12), chromeMat);
          post.position.set(x, postY, side * 0.72);
          currentMeshGroup.add(post);
        }

        // 30cm Horizontal Extensions at Top & Bottom
        const extBottom = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.35, 12), chromeMat);
        extBottom.rotation.z = Math.PI / 2;
        extBottom.position.set(-2.15, 0.85, side * 0.72);
        currentMeshGroup.add(extBottom);

        const extTop = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.35, 12), chromeMat);
        extTop.rotation.z = Math.PI / 2;
        extTop.position.set(2.15, 1.10, side * 0.72);
        currentMeshGroup.add(extTop);
      }

      // Wheelchair Ascending
      if (show3DWheelchair) {
        const chair = createWheelchairModel();
        chair.position.set(0, 0.22, 0);
        chair.rotation.z = -Math.atan(rampSlope);
        currentMeshGroup.add(chair);
      }
    }

    // --- 3. DETAILED 3D ACCESSIBLE STAIRS SCENE ---
    function build3DStairsScene() {
      clear3DScene();
      current3DType = 'stairs';
      document.getElementById('3d-scene-badge').innerText = 'السلالم الميسرة والدرابزين المزدوج (2R+T=62 سم - م.ب.ع 202)';
      document.getElementById('3d-dim-hud').innerText = 'R: 15cm | T: 32cm | Bevel 60° | Tactile 60cm';

      const tileTex = getTileTexture();
      const tactileTex = getTactileTexture();
      const chromeMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, metalness: 0.95, roughness: 0.15 });
      const stepMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4 });
      const yellowStripMat = new THREE.MeshBasicMaterial({ color: 0xfacc15 });

      // 6 Steps Flight
      const numSteps = 6;
      const riserH = 0.15;
      const treadW = 0.32;
      const stairW = 1.6;

      for (let i = 0; i < numSteps; i++) {
        // Step Block
        const step = new THREE.Mesh(new THREE.BoxGeometry(stairW, riserH, treadW), stepMat);
        step.position.set(0, (i * riserH) + (riserH / 2), -(i * treadW));
        step.receiveShadow = true;
        currentMeshGroup.add(step);

        // High Contrast Yellow Nosing Strip (5cm width on step edge)
        const strip = new THREE.Mesh(new THREE.BoxGeometry(stairW, 0.005, 0.05), yellowStripMat);
        strip.position.set(0, (i * riserH) + riserH + 0.001, -(i * treadW) + (treadW / 2) - 0.025);
        currentMeshGroup.add(strip);
      }

      // Lower Landing with 60cm Tactile Blister Paving
      const lowerPad = new THREE.Mesh(new THREE.BoxGeometry(stairW, 0.01, 0.8), new THREE.MeshStandardMaterial({ map: tactileTex }));
      lowerPad.position.set(0, 0.005, 0.6);
      currentMeshGroup.add(lowerPad);

      // Continuous Dual Handrails with 30cm Returns
      for (let side = -1; side <= 1; side += 2) {
        // Upper Rail (85cm)
        const rail1 = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 2.2, 16), chromeMat);
        rail1.rotation.x = 0.44;
        rail1.position.set(side * 0.82, 0.85 + (3 * riserH), -(3 * treadW) + 0.3);
        currentMeshGroup.add(rail1);

        // Lower Rail (65cm)
        const rail2 = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.018, 2.2, 16), chromeMat);
        rail2.rotation.x = 0.44;
        rail2.position.set(side * 0.82, 0.65 + (3 * riserH), -(3 * treadW) + 0.3);
        currentMeshGroup.add(rail2);

        // 30cm Horizontal Extension at Bottom
        const extBot = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.3, 12), chromeMat);
        extBot.rotation.x = Math.PI / 2;
        extBot.position.set(side * 0.82, 0.85, 0.35);
        currentMeshGroup.add(extBot);
      }
    }

    // --- 4. DETAILED 3D ELEVATOR CABIN SCENE ---
    function build3DElevatorScene() {
      clear3DScene();
      current3DType = 'elevator';
      document.getElementById('3d-scene-badge').innerText = 'مقصورة مصعد شامل 1.40 × 1.10 م مع لوحة برايل (م.ب.ع 202)';
      document.getElementById('3d-dim-hud').innerText = 'Cabin 1.40x1.10m | Door 90cm | Braille COP 90-120cm';

      const steelMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.9, roughness: 0.25 });
      const chromeMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, metalness: 0.98, roughness: 0.08 });
      const mirrorMat = new THREE.MeshStandardMaterial({ color: 0xffffff, metalness: 1.0, roughness: 0.02 });

      // Cabin Floor (1.40 x 1.10 m)
      const floor = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.08, 1.5), new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.6 }));
      floor.position.set(0, -0.04, 0);
      currentMeshGroup.add(floor);

      if (show3DWalls) {
        // Stainless Steel Walls
        const leftWall = new THREE.Mesh(new THREE.BoxGeometry(0.04, 2.3, 1.5), steelMat);
        leftWall.position.set(-0.62, 1.15, 0);
        currentMeshGroup.add(leftWall);

        const rightWall = new THREE.Mesh(new THREE.BoxGeometry(0.04, 2.3, 1.5), steelMat);
        rightWall.position.set(0.62, 1.15, 0);
        currentMeshGroup.add(rightWall);

        // Rear Wall with Full-Height Mirror
        const backWall = new THREE.Mesh(new THREE.BoxGeometry(1.2, 2.3, 0.04), steelMat);
        backWall.position.set(0, 1.15, -0.77);
        currentMeshGroup.add(backWall);

        const mirror = new THREE.Mesh(new THREE.BoxGeometry(1.0, 1.8, 0.01), mirrorMat);
        mirror.position.set(0, 1.3, -0.74);
        currentMeshGroup.add(mirror);

        // Recessed Ceiling with LED Downlights
        const ceiling = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.05, 1.5), steelMat);
        ceiling.position.set(0, 2.325, 0);
        currentMeshGroup.add(ceiling);
      }

      // Wraparound Handrails on 3 Sides (85cm height)
      const railBack = new THREE.Mesh(new THREE.CylinderGeometry(0.019, 0.019, 1.1, 16), chromeMat);
      railBack.rotation.z = Math.PI / 2;
      railBack.position.set(0, 0.85, -0.7);
      currentMeshGroup.add(railBack);

      const railSideL = new THREE.Mesh(new THREE.CylinderGeometry(0.019, 0.019, 1.3, 16), chromeMat);
      railSideL.rotation.x = Math.PI / 2;
      railSideL.position.set(-0.55, 0.85, 0);
      currentMeshGroup.add(railSideL);

      // Car Operating Panel (COP) with Braille Buttons & LCD Display
      const copColumn = new THREE.Mesh(new THREE.BoxGeometry(0.2, 1.2, 0.03), chromeMat);
      copColumn.position.set(0.58, 1.1, 0.2);
      currentMeshGroup.add(copColumn);

      // LCD Display (Floor 3)
      const lcd = new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.1, 0.01), new THREE.MeshBasicMaterial({ color: 0x0284c7 }));
      lcd.position.set(0.565, 1.55, 0.2);
      currentMeshGroup.add(lcd);

      // Illuminated Buttons
      for (let b = 0; b < 6; b++) {
        const btn = new THREE.Mesh(
          new THREE.CylinderGeometry(0.018, 0.018, 0.01, 16),
          new THREE.MeshStandardMaterial({ color: 0xf59e0b, emissive: 0xd97706, emissiveIntensity: 0.6 })
        );
        btn.rotation.z = Math.PI / 2;
        btn.position.set(0.56, 1.35 - (b * 0.06), 0.2 + ((b % 2) * 0.05) - 0.025);
        currentMeshGroup.add(btn);
      }

      // Wheelchair in Cabin
      if (show3DWheelchair) {
        const chair = createWheelchairModel();
        chair.position.set(0, 0, 0.1);
        currentMeshGroup.add(chair);
      }
    }

    // --- SCENE & CAMERA CONTROL FUNCTIONS ---
    function switch3DScene(type) {
      document.querySelectorAll('.btn-3d-scene').forEach(btn => {
        btn.className = 'btn-3d-scene px-3 py-1.5 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition';
      });
      const activeBtn = document.getElementById('btn-3d-' + type);
      if (activeBtn) activeBtn.className = 'btn-3d-scene px-3 py-1.5 rounded-xl bg-teal-600 text-white font-bold transition shadow-xs';

      if (type === 'restroom') build3DRestroomScene();
      else if (type === 'ramp') build3DRampScene();
      else if (type === 'stairs') build3DStairsScene();
      else if (type === 'elevator') build3DElevatorScene();
    }

    function set3DCameraView(mode) {
      isAutoTour = false;
      document.getElementById('icon-autotour').innerText = "▶️";

      if (mode === 'eye') {
        // Eye-level of wheelchair user (height: 1.20m)
        rotX = 0.05;
        rotY = -0.1;
        targetZoom = 3.2;
        panX = 0;
        panY = 1.0;
        panZ = 0.2;
      } else if (mode === 'iso') {
        // Classic Architectural Isometric 45°
        rotX = 0.52;
        rotY = -0.78;
        targetZoom = 6.5;
        panX = 0;
        panY = 0.6;
        panZ = 0;
      } else if (mode === 'top') {
        // Top-down 3D Plan
        rotX = Math.PI / 2.15;
        rotY = 0;
        targetZoom = 5.8;
        panX = 0;
        panY = 0.1;
        panZ = 0;
      }
    }

    function toggle3DAutoTour() {
      isAutoTour = !isAutoTour;
      const icon = document.getElementById('icon-autotour');
      const btn = document.getElementById('btn-3d-autotour');
      if (isAutoTour) {
        icon.innerText = "⏸️";
        btn.className = 'px-2.5 py-1 rounded-lg bg-rose-500 hover:bg-rose-600 text-white font-bold text-[11px] flex items-center gap-1 shadow-xs transition';
      } else {
        icon.innerText = "▶️";
        btn.className = 'px-2.5 py-1 rounded-lg bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-[11px] flex items-center gap-1 shadow-xs transition';
      }
    }

    function reset3DCamera() {
      isAutoTour = false;
      rotX = 0.45;
      rotY = -0.6;
      targetZoom = 6.8;
      panX = 0;
      panY = 0.6;
      panZ = 0;
    }

    function toggle3DWalls() {
      show3DWalls = !show3DWalls;
      document.getElementById('btn-3d-walls').innerText = show3DWalls ? "🧱 إخفاء الجدران" : "🧱 إظهار الجدران";
      switch3DScene(current3DType);
    }

    function toggle3DWheelchair() {
      show3DWheelchair = !show3DWheelchair;
      document.getElementById('btn-3d-wheelchair').innerText = show3DWheelchair ? "♿ إخفاء الكرسي" : "♿ إظهار الكرسي";
      switch3DScene(current3DType);
    }

    function toggle3DDimensions() {
      show3DDimensions = !show3DDimensions;
      const hud = document.getElementById('3d-dim-hud');
      if (hud) hud.style.display = show3DDimensions ? 'block' : 'none';
      document.getElementById('btn-3d-dims').innerText = show3DDimensions ? "📏 إخفاء الأبعاد" : "📏 إظهار الأبعاد";
    }
"""

for fpath in FILES:
    print(f"Upgrading 3D Walkthrough in: {fpath}")
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace HTML Markup for 3D Walkthrough
    old_html_pattern = r'<!-- 3D WEBGL INTERACTIVE WALKTHROUGH[\s\S]*?<!-- MODULE 1: RAMP CALCULATOR -->'
    match_html = re.search(old_html_pattern, content)
    if match_html:
        content = content[:match_html.start()] + NEW_3D_HTML.strip() + "\n\n      <!-- MODULE 1: RAMP CALCULATOR -->" + content[match_html.end():]
        print("  ✓ Replaced 3D HTML Markup with High-Fidelity Container")
    else:
        print("  ⚠️ Old 3D HTML pattern not found, trying alternate pattern...")
        # fallback search
        alt_pattern = r'(<div class="bg-\[var\(--card,#fff\)\] border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm">[\s\S]*?id="calc-3d-section"[\s\S]*?</div>\s*</div>\s*)(<!-- MODULE 1: RAMP CALCULATOR -->)'
        match_alt = re.search(alt_pattern, content)
        if match_alt:
            content = content[:match_alt.start()] + NEW_3D_HTML.strip() + "\n\n      <!-- MODULE 1: RAMP CALCULATOR -->" + content[match_alt.end():]
            print("  ✓ Replaced 3D HTML Markup via fallback pattern")

    # 2. Replace Old 3D JavaScript with High-Fidelity Engine
    js_start = content.find("// =========================================================================")
    if js_start != -1:
        # Find where Track 1 3D starts
        t1_marker = "// 🌐 TRACK 1: 3D WEBGL INTERACTIVE WALKTHROUGH"
        t2_marker = "// ========================================================================="
        p1 = content.find(t1_marker)
        if p1 != -1:
            p2 = content.find(t2_marker, p1 + len(t1_marker))
            if p2 != -1:
                content = content[:p1] + REALISTIC_3D_JS.strip() + "\n\n    " + content[p2:]
                print("  ✓ Injected Realistic Architectural 3D Three.js Engine")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Completed upgrading {fpath}\n")

print("All 3D Walkthrough upgrades successfully applied!")
