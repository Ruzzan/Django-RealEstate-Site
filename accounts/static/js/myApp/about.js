function changeBackgroundImage() {
    var images = [
    "url('https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?cs=srgb&dl=apartment-architectural-design-architecture-323780.jpg&fm=jpg')",
    
    "url('https://images.pexels.com/photos/323776/pexels-photo-323776.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940')",

    "url('https://images.pexels.com/photos/323772/pexels-photo-323772.jpeg?cs=srgb&dl=apartment-architectural-design-architecture-323772.jpg&fm=jpg')",

    "url('https://images.pexels.com/photos/534182/pexels-photo-534182.jpeg?cs=srgb&dl=architecture-balcony-building-534182.jpg&fm=jpg')",
    ];

    let randomImg = Math.floor(Math.random() * images.length);

    document.querySelector('#about-head').style.backgroundImage = images[randomImg];

    

 
}

changeBackgroundImage();


