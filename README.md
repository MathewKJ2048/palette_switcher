# Palette Switcher
A python script to identify and change the color palette of arbitrary images

## Pre-requisites:

- python 3
- numpy
- PIL
- scikit-learn

## Use:

Run `main.py` with one of the following arguments:

  <style>
    body {
      margin: 0;
      overflow: hidden;
    }

    #slideshow-container {
      display: flex;
      width: 100%;
      height: 100vh;
      overflow: hidden;
    }

    .slide {
      flex: 1;
      display: none;
      align-items: center;
      justify-content: center;
      text-align: center;
    }

    img {
      max-width: 100%;
      max-height: 100%;
    }

    #prev, #next {
      position: absolute;
      top: 50%;
      width: auto;
      padding: 16px;
      margin-top: -22px;
      font-size: 24px;
      cursor: pointer;
      color: white;
      background-color: rgba(0, 0, 0, 0.5);
      border: none;
    }

    #prev {
      left: 0;
    }

    #next {
      right: 0;
    }
  </style>
</head>
<body>

<div id="slideshow-container">
  <div class="slide">
    <img src="image1.jpg" alt="Image 1">
  </div>
  <div class="slide">
    <img src="image2.jpg" alt="Image 2">
  </div>
  <div class="slide">
    <img src="image3.jpg" alt="Image 3">
  </div>
  <!-- Add more slides as needed -->

  <button id="prev" onclick="plusSlides(-1)">❮</button>
  <button id="next" onclick="plusSlides(1)">❯</button>
</div>

<script>
  let slideIndex = 1;
  showSlides(slideIndex);

  function plusSlides(n) {
    showSlides(slideIndex += n);
  }

  function currentSlide(n) {
    showSlides(slideIndex = n);
  }

  function showSlides(n) {
    let i;
    const slides = document.getElementsByClassName("slide");

    if (n > slides.length) {
      slideIndex = 1;
    }

    if (n < 1) {
      slideIndex = slides.length;
    }

    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }

    slides[slideIndex - 1].style.display = "flex";
  }
</script>

