import os
from pathlib import Path
import pillow_heif
from PIL import Image

# ── Configuration ─────────────────────────────────────────────────────────────
SOURCE_FOLDER  = r"D:\202603_a"           # Folder containing .HEIC files
OUTPUT_FORMAT  = "JPG"                    # Change to "PNG" if you prefer PNG
QUALITY        = 95                       # JPG quality (1–95). Ignored for PNG.
# ──────────────────────────────────────────────────────────────────────────────

# Register HEIF/HEIC support with Pillow
pillow_heif.register_heif_opener()

def get_output_folder(source: str, fmt: str) -> Path:
    """Creates a sibling folder named  <source>_converted_<FORMAT>."""
    src = Path(source)
    out = src.parent / f"{src.name}_converted_{fmt.upper()}"
    out.mkdir(parents=True, exist_ok=True)
    return out

def convert_heic_files(source_folder: str, output_format: str, quality: int):
    src_path = Path(source_folder)

    if not src_path.exists():
        print(f"[ERROR] Source folder not found: {source_folder}")
        return

    # Collect all .heic / .HEIC files (case-insensitive)
    heic_files = [f for f in src_path.iterdir()
                  if f.suffix.lower() == ".heic" and f.is_file()]

    if not heic_files:
        print(f"[INFO] No .HEIC files found in: {source_folder}")
        return

    out_path = get_output_folder(source_folder, output_format)
    ext = ".jpg" if output_format.upper() in ("JPG", "JPEG") else ".png"
    save_format = "JPEG" if ext == ".jpg" else "PNG"

    print(f"\n  Source  : {src_path}")
    print(f"  Output  : {out_path}")
    print(f"  Format  : {save_format}")
    print(f"  Files   : {len(heic_files)} found\n")
    print("-" * 50)

    success = 0
    failed  = 0

    for i, heic_file in enumerate(sorted(heic_files), start=1):
        out_file = out_path / (heic_file.stem + ext)
        try:
            with Image.open(heic_file) as img:
                # Convert to RGB so JPG doesn't choke on transparency/palette modes
                if img.mode not in ("RGB", "L"):
                    img = img.convert("RGB")

                save_kwargs = {"format": save_format}
                if save_format == "JPEG":
                    save_kwargs["quality"] = quality
                    save_kwargs["subsampling"] = 0   # best chroma quality

                img.save(out_file, **save_kwargs)

            print(f"  [{i:>3}/{len(heic_files)}] ✓  {heic_file.name}  →  {out_file.name}")
            success += 1

        except Exception as e:
            print(f"  [{i:>3}/{len(heic_files)}] ✗  {heic_file.name}  — ERROR: {e}")
            failed += 1

    print("-" * 50)
    print(f"\n  Done!  ✓ {success} converted   ✗ {failed} failed")
    print(f"  Saved to: {out_path}\n")


if __name__ == "__main__":
    convert_heic_files(SOURCE_FOLDER, OUTPUT_FORMAT, QUALITY)