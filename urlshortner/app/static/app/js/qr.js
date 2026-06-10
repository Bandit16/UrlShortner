document.querySelectorAll('[data-qr-url]').forEach(el => {
    new QRCode(el, {
        text: el.dataset.qrUrl,
        width: 120,
        height: 120,
        colorDark: '#18283b',
        colorLight: '#ffffff',
    });
});
