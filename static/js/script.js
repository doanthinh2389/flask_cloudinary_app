document.addEventListener('DOMContentLoaded', function() {
    // Copy link functionality
    document.querySelectorAll('.copy-link').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.getAttribute('data-url');
            navigator.clipboard.writeText(url)
                .then(() => {
                    const originalText = this.innerHTML;
                    this.innerHTML = '<i class="bi bi-check"></i> Copied!';
                    setTimeout(() => {
                        this.innerHTML = originalText;
                    }, 2000);
                })
                .catch(err => {
                    console.error('Could not copy text: ', err);
                });
        });
    });

    // File input preview
    const fileInput = document.getElementById('fileInput');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const fileSize = file.size / 1024 / 1024; // in MB
                if (fileSize > 5) {
                    alert('File size exceeds 5MB limit. Please choose a smaller file.');
                    this.value = '';
                }
            }
        });
    }
});