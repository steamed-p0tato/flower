import streamlit as st
import streamlit.components.v1 as components

def get_css():
    return """
    <style>
    #MainMenu, header, footer { visibility: hidden; }
    .stDeployButton { display: none; }
    body { height: 100%; width: 100%; background: #0b152b !important; overflow: hidden; margin: 0; }
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
    }
    .star {
        position: absolute;
        background: white;
        border-radius: 50%;
        animation: twinkle var(--duration) infinite;
    }
    .bottom-text {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        color: #CE395B;
        font-family: 'Palatino', serif;
        font-size: 2em;
        font-weight: bold;
        text-shadow: 
            0px 0px 10px rgba(255, 59, 48, 0.8),
            0px 0px 20px rgba(255, 59, 48, 0.6),
            0px 0px 30px rgba(255, 59, 48, 0.4);
        letter-spacing: 1px;
        opacity: 0;
        animation: fadeIn 4s ease-out forwards, moveUp 4s ease-out forwards;
        z-index: 9999;
    }
    .container {
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }
    .glass {
        height: 350px;
        width: 200px;
        background: #122139;
        border-radius: 300px 300px 0px 0px;
        position: relative;
    }
    .glass:before {
        content: "";
        height: 10px;
        width: 10px;
        transform-origin: center;
        border: 10px solid #122139;
        border-radius: 100%;
        position: absolute;
        left: 87px;
        top: -25px;
    }
    .glass:after {
        content: "";
        position: absolute;
        height: 15px;
        width: 250px;
        background: #a52a2a;
        top: 100%;
        left: -13%;
    }
    .shine {
        width: 12px;
        height: 140px;
        background: white;
        opacity: 0.2;
        position: absolute;
        left: 85%;
        top: 80px;
        border-radius: 100px;
        z-index: 10;
    }
    .shine:before {
        content: "";
        width: 12px;
        height: 20px;
        position: absolute;
        background: white;
        top: 160px;
        border-radius: 100px;
    }
    .petals > div {
        position: absolute;
        background: #d52d58;
        width: 45px;
        height: 80px;
        top: 55px;
        transition: all 0.5s ease-out;
    }
    .petals > div:nth-child(1) {
        border-radius: 15px;
        box-shadow: 0px 0px 30px rgba(245, 148, 184, 1);
        left: 80px;
        top: 60px;
        background: #d52d58;
    }
    .petals > div:nth-child(2),
    .petals > div:nth-child(4),
    .petals > div:nth-child(6) {
        background: #b81b43;
        left: 60px;
        border-radius: 0px 30px 0px 30px;
        transform-origin: bottom right;
    }
    .petals > div:nth-child(3),
    .petals > div:nth-child(5),
    .petals > div:nth-child(7) {
        background: #b81b43;
        left: 100px;
        border-radius: 30px 0px 30px 0px;
        transform-origin: bottom left;
    }
    .petals > div:nth-child(2) {
        background: #a31c3d;
        top: 75px;
        height: 70px;
        box-shadow: 0px 0px 50px rgba(245, 148, 184, .5);
        z-index: 5;
        animation: bloom2 3s ease-in-out forwards;
    }
    .petals > div:nth-child(3) {
        background: #a31c3d;
        top: 75px;
        height: 70px;
        box-shadow: 0px 0px 50px rgba(245, 148, 184, .5);
        z-index: 4;
        animation: bloom3 3s ease-in-out, glowing 2.5s ease-in-out infinite;
        animation-fill-mode: forwards;
    }
    .petals > div:nth-child(4) {
        background: #b81b43;
        top: 70px;
        height: 75px;
        box-shadow: 0px 0px 50px rgba(245, 148, 184, .5);
        z-index: 3;
        animation: bloom4 3s ease-in-out, glowing 2.5s ease-in-out infinite;
        animation-fill-mode: forwards;
    }
    .petals > div:nth-child(5) {
        background: #b81b43;
        top: 70px;
        height: 75px;
        box-shadow: 0px 0px 50px rgba(245, 148, 184, .5);
        z-index: 2;
        animation: bloom5 3s ease-in-out, glowing 2.5s ease-in-out infinite;
        animation-fill-mode: forwards;
    }
    .petals > div:nth-child(6) {
        background: #c9204b;
        top: 65px;
        height: 70px;
        box-shadow: 0px 0px 50px rgba(245, 148, 184, .3);
        z-index: 1;
        animation: bloom6 3s ease-in-out, glowing 2.5s ease-in-out infinite;
        animation-fill-mode: forwards;
    }
    .petals > div:nth-child(7) {
        background: #c9204b;
        top: 65px;
        height: 70px;
        box-shadow: 0px 0px 50px rgba(245, 148, 184, .3);
        z-index: 0;
        animation: bloom7 3s ease-in-out, glowing 2.5s ease-in-out infinite;
        animation-fill-mode: forwards;
    }
    .deadPetals > div {
        position: absolute;
        background: #d52d58;
        width: 20px;
        height: 15px;
        top: 120px;
        border-radius: 0px 30px 0px 30px;
        box-shadow: 0px 0px 30px rgba(245, 148, 184, .5);
        transition: all 0.5s ease-out;
    }
    .deadPetals > div:nth-child(1) { left: 85px; transform: rotate(-30deg); animation: falling 20s 4s ease-in-out infinite; }
    .deadPetals > div:nth-child(2) { left: 100px; transform: rotate(-30deg); animation: falling 20s 8s ease-in-out infinite; }
    .deadPetals > div:nth-child(3) { left: 110px; transform: rotate(-30deg); animation: falling 20s 12s ease-in-out infinite; }
    .deadPetals > div:nth-child(4) { left: 90px; transform: rotate(-30deg); animation: falling 20s 16s ease-in-out infinite; }
    .leaves > div:nth-last-child(1) {
        position: absolute;
        width: 55px;
        height: 30px;
        background: #338f37;
        top: 120px;
        left: 75px;
        border-radius: 100px;
    }
    .leaves > div:nth-child(1) {
        position: absolute;
        width: 6px;
        height: 210px;
        background: #055905;
        top: 95px;
        left: 100px;
        border-radius: 0 0 100px 100px;
    }
    .leaves > div:nth-child(2) {
        position: absolute;
        width: 30px;
        height: 50px;
        border-radius: 5px 40px 20px 40px;
        background: #055905;
        transform-origin: bottom;
        transform: rotate(-30deg);
        top: 180px;
        left: 80px;
        box-shadow: inset 5px 5px #066406;
    }
    .leaves > div:nth-child(3) {
        position: absolute;
        width: 30px;
        height: 50px;
        border-radius: 40px 5px 40px 20px;
        background: #055905;
        transform-origin: bottom;
        transform: rotate(30deg);
        top: 150px;
        left: 95px;
        box-shadow: inset -5px 5px #066406;
    }
    .thorns > div {
        position: absolute;
        width: 0;
        height: 0;
        top: 140px;
    }
    .thorns > div:nth-child(odd) {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        border-left: 5px solid #055905;
        left: 105px;
    }
    .thorns > div:nth-child(even) {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        border-right: 5px solid #055905;
        left: 95px;
    }
    .thorns > div:nth-child(1) { top: 200px; }
    .thorns > div:nth-child(2) { top: 170px; }
    .thorns > div:nth-child(4) { top: 230px; }
    @keyframes bloom2 {
        50% {
            transform: rotate(-90deg);
            top: 200px;
            left: 100px;
        }
        100% {
            transform: rotate(-60deg);
            top: 252px;
            left: 50px;
            background: #651026;
            box-shadow: 0px 0px 0px rgba(245, 148, 184, 0);
        }
    }
    @keyframes bloom3 { 100% { transform: rotate(45deg); } }
    @keyframes bloom4 { 100% { transform: rotate(-20deg); } }
    @keyframes bloom5 { 100% { transform: rotate(20deg); } }
    @keyframes bloom6 { 100% { transform: rotate(-5deg); } }
    @keyframes bloom7 { 100% { transform: rotate(5deg); } }
    @keyframes glowing {
        50% {
            background: #d94563;
            box-shadow: 0px 0px 60px rgba(245, 148, 184, 1);
        }
    }
    @keyframes falling {
        20% {
            top: 335px;
            background: #a31a3e;
            box-shadow: 0px 0px 0px rgba(245, 148, 184, 0);
        }
        100% {
            top: 335px;
            opacity: 0;
        }
    }
    @keyframes twinkle {
        0%, 100% { opacity: 0.2; }
        50% { opacity: 1; }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes moveUp {
        0% { transform: translateX(-50%) translateY(20px); }
        100% { transform: translateX(-50%) translateY(0); }
    }
    </style>
    """

def get_html():
    return """
    <div class="stars" id="stars"></div>
    <div class="container">
        <div class="glass">
            <div class="shine"></div>
        </div>
        <div class="thorns">
            <div></div><div></div><div></div><div></div>
        </div>
        <div class="leaves">
            <div></div><div></div><div></div><div></div>
        </div>
        <div class="petals">
            <div></div><div></div><div></div><div></div>
            <div></div><div></div><div></div>
        </div>
        <div class="deadPetals">
            <div></div><div></div><div></div><div></div>
        </div>
    </div>
    <div class="bottom-text">for my Goldfish</div>
    <script>
        const starsContainer = document.getElementById('stars');
        for (let i = 0; i < 200; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.width = Math.random() * 3 + 'px';
            star.style.height = star.style.width;
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.setProperty('--duration', (Math.random() * 3 + 2) + 's');
            star.style.opacity = Math.random();
            starsContainer.appendChild(star);
        }
    </script>
    """

def main():
    st.set_page_config(page_title="Animated Rose", layout="wide")
    components.html(f"<!DOCTYPE html><html><head>{get_css()}</head><body>{get_html()}</body></html>", height=800)

if __name__ == "__main__":
    main()