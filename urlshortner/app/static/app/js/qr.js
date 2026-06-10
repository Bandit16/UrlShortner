const dateTimeFormatter = new Intl.DateTimeFormat(undefined, {
    dateStyle: 'medium',
    timeStyle: 'short',
});

document.querySelectorAll('[data-qr-url]').forEach((el) => {
    new QRCode(el, {
        text: el.dataset.qrUrl,
        width: 120,
        height: 120,
        colorDark: '#18283b',
        colorLight: '#ffffff',
    });
});

document.querySelectorAll('[data-link-meta]').forEach((meta) => {
    const expiryNode = meta.querySelector('[data-expiry-at]');
    const createdNode = meta.querySelector('[data-created-at]');

    if (expiryNode?.dataset.expiryAt) {
        const expiryDate = new Date(expiryNode.dataset.expiryAt);
        expiryNode.innerHTML = `<i class="fas fa-calendar-day"></i> Expires ${dateTimeFormatter.format(expiryDate)}`;
    }

    if (createdNode?.dataset.createdAt) {
        const createdDate = new Date(createdNode.dataset.createdAt);
        createdNode.innerHTML = `<i class="fas fa-calendar"></i> Created ${dateTimeFormatter.format(createdDate)}`;
    }
});

document.querySelectorAll('[data-copy-code]').forEach((button) => {
    button.addEventListener('click', async () => {
        const code = button.dataset.copyCode;
        if (!code) {
            return;
        }

        try {
            await navigator.clipboard.writeText(code);
            const originalHtml = button.innerHTML;
            button.classList.add('is-copied');
            button.innerHTML = '<i class="fas fa-check"></i>';

            window.setTimeout(() => {
                button.innerHTML = originalHtml;
                button.classList.remove('is-copied');
            }, 1400);
        } catch (error) {
            console.error('Unable to copy code', error);
        }
    });
});

document.querySelectorAll('[data-copy-url]').forEach((button) => {
    button.addEventListener('click', async () => {
        const url = button.dataset.copyUrl;
        if (!url) {
            return;
        }

        try {
            await navigator.clipboard.writeText(url);
            const originalHtml = button.innerHTML;
            button.classList.add('is-copied');
            button.innerHTML = '<i class="fas fa-check"></i>';

            window.setTimeout(() => {
                button.innerHTML = originalHtml;
                button.classList.remove('is-copied');
            }, 1400);
        } catch (error) {
            console.error('Unable to copy url', error);
        }
    });
});
