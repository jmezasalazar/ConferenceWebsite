anime({
    targets: 'div.box.red',
    translateY: [
        {value: 200, duration: 3000},
        {value: 0, duration: 800}

    ],
    rotate: {
        value: '1turn',
        easing: 'easeInOutSine'
    }

});

anime({
    targets: '#svgAttributes polygon',
    points: '64 128 8.574 96 8.574 32 64 0 119.426 32 119.426 96',
    easing: 'easeInOutExpo',
    duration: 1000,
    loop: true
});