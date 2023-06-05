# photos-sort
Sort photos in a folder by day and month.

## How to use
1. Fix metadata (for example if exported from iCloud)
    - Images:
        `exiftool '-FileModifyDate<DateTimeOriginal' .`
    - Videos:
        `exiftool '-FileModifyDate<CreationDate' -ext .mov .`
        `exiftool '-FileModifyDate<CreationDate' -ext .mp4 .`
2. Put everything in right folder
3. Adapt folder in script
4. Run script
5. Eventually rename folders to highlights or important moments captured