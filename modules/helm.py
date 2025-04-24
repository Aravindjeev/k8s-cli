import os
import platform
import shutil
import tarfile
import zipfile
import tempfile
import urllib.request

def install_helm():
    system = platform.system().lower()
    arch = platform.machine().lower()
    if arch in ["x86_64", "amd64"]:
        arch = "amd64"


    # if "x86_64" in arch:
    #     arch = "amd64"

    version = "v3.7.0"
    helm_base_url = f"https://get.helm.sh/helm-{version}-{system}-{arch}"

    # Set file extensions for platform
    ext = ".zip" if system == "windows" else ".tar.gz"
    filename = f"helm{ext}"

    # Download Helm archive
    try:
        print(f"Downloading {helm_base_url}{ext}...")
        urllib.request.urlretrieve(f"{helm_base_url}{ext}", filename)
    except Exception as e:
        raise Exception(f"Failed to download Helm: {str(e)}")

    # Extract and move helm binary
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            if ext == ".tar.gz":
                with tarfile.open(filename, "r:gz") as tar:
                    tar.extractall(path=tmpdir)
                helm_src = os.path.join(tmpdir, f"{system}-{arch}", "helm")
            else:
                with zipfile.ZipFile(filename, 'r') as zip_ref:
                    zip_ref.extractall(tmpdir)
                helm_src = os.path.join(tmpdir, "windows-amd64", "helm.exe")

            helm_dest = shutil.which("helm") or os.path.join(os.getcwd(), "helm.exe" if system == "windows" else "helm")
            shutil.move(helm_src, helm_dest)
            os.chmod(helm_dest, 0o755)
            return f"✅ Helm installed at {helm_dest}"
    except Exception as e:
        raise Exception(f"Failed to extract and install Helm: {str(e)}")
