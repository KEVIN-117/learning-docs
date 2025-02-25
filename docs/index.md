<div style="position: rekative; width: 100%; height: 80vh;">
  <div style="
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  justify-content: center;
  align-items: start;
  padding: 20px;
  background: linear-gradient(135deg, #0d1117 0%, #1a2331 100%);
  position: absolute;
">
  <!-- Contenido Original -->
  <div style="display: grid; gap: 20px;">
		<div style="
    background: linear-gradient(135deg, #1a2331 0%, #0d1117 100%);
    color: #e0e0e0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 40px;
    text-align: center;
    flex: 1;
    min-width: 300px;
    max-width: 800px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
  " onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
    <div style="
      position: absolute;
      top: -50px;
      left: -50px;
      width: 100px;
      height: 100px;
      background: radial-gradient(circle, #9fef0033 0%, transparent 70%);
      border-radius: 50%;
    "></div>
    
    <h1 style="
      color: #9fef00;
      font-size: 3em;
      margin-bottom: 30px;
      text-shadow: 0 2px 4px rgba(0,0,0,0.3);
      position: relative;
      z-index: 1;
      transition: all 0.3s ease;
    " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
      Bienvenido a mi viaje tecnológico
    </h1>
    
    <p style="
      font-size: 1.2em;
      line-height: 1.8;
      margin-bottom: 30px;
      background: rgba(255,255,255,0.05);
      padding: 20px;
      border-radius: 15px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    ">
      Acompáñenme a explorar el vasto mundo de la tecnología. Desde la creación de sistemas backend eficientes hasta la inmersión en el mundo de la IA, mi misión es convertirme en un desarrollador completo.
    </p>
    
    <p style="
      color: #5af78e;
      font-size: 1.3em;
      margin-bottom: 40px;
      font-weight: bold;
      text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    ">
      ¡Descubra conocimientos sobre backend, IA, DevOps, front-end, redes y seguridad!
    </p>
    
    <p style="
      color: #a4b1cd;
      font-size: 1em;
      margin-top: 40px;
      font-style: italic;
      position: relative;
      z-index: 1;
    ">
      Recuerda: todo experto fue alguna vez un principiante. ¡Aprendamos y crezcamos juntos!
    </p>

    <div style="
      position: absolute;
      bottom: -30px;
      right: -30px;
      width: 80px;
      height: 80px;
      background: radial-gradient(circle, #5af78e33 0%, transparent 70%);
      border-radius: 50%;
    "></div>
  </div>
		<div style="
    background: linear-gradient(135deg, #1a2331 0%, #0d1117 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 5px;
    text-align: center;
    flex: 1;
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    animation: borderGlow 3s infinite;
">
    <style>
        @keyframes borderGlow {
            0% {
                box-shadow: 0 0 20px #008cffb9,
                            inset 0 0 20px #008cffb9;
            }
            50% {
                box-shadow: 0 0 40px #008cffb9,
                            inset 0 0 40px #008cffb9;
            }
            100% {
                box-shadow: 0 0 20px #008cffb9,
                            inset 0 0 20px #008cffb9;
            }
        }

        @keyframes textGlow {
            0% {
                filter: drop-shadow(0 0 2px #1a23) drop-shadow(0 0 4px #9fef00);
            }
            50% {
                filter: drop-shadow(0 0 8px #1a23) drop-shadow(0 0 12px #9fef00);
            }
            100% {
                filter: drop-shadow(0 0 2px #1a23) drop-shadow(0 0 4px #9fef00);
            }
        }

        .gradient-border {
            position: relative;
            z-index: 0;
        }

        .gradient-border::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            z-index: -1;
            background: linear-gradient(45deg,
				    #1c2635,
				    #1a23,
				    #42a4f554,
				    #1c2635,
				    #1a23,
				    #42a4f554,
				    #1c2635);
            background-size: 400%;
            border-radius: 22px;
            animation: gradientBorder 20s linear infinite;
        }

        .gradient-text {
            background: linear-gradient(
                135deg,
                #9fef00 0%,
                #5af78e 25%,
                #42a5f5 50%,
                #9fef00 75%,
                #5af78e 100%
            );
            background-size: 200% auto;
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textGlow 3s infinite;
        }
    </style>

    <div class="gradient-border" style="
        background: linear-gradient(135deg, rgba(26, 35, 49, 0.9) 0%, rgba(13, 17, 23, 0.9) 100%);
        border-radius: 20px;
        padding: 10px;
        transition: transform 0.3s ease;
    " onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
        <p class="gradient-text" style="
            font-size: 4em;
            font-style: italic;
            font-weight: bold;
            margin: 0;
            padding: 10px;
            position: relative;
            z-index: 1;
            letter-spacing: 2px;
        ">
            h4ck4u 1i8n
        </p>
    </div>
</div>
 </div>

  <!-- Imagen del Samurái -->
  <div style="
    flex: 0 1 345px;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    background: linear-gradient(135deg, #1a2331 0%, #0d1117 100%);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease;
  " onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
    <img 
      src="https://res.cloudinary.com/disvwilxi/image/upload/v1712914497/ypvscctuqxlbfzyz39z0.jpg"
      alt="Samurái con sable láser bajo un árbol de cerezo"
      style="
        width: 100%;
        height: auto;
        border-radius: 15px;
        object-fit: contain;
      "
    />
  </div>
</div>

</div>