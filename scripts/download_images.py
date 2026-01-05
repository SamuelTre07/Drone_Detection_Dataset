from bing_image_downloader import downloader

def BingBatchDownload(keyword, num_images, output_dir):
    downloader.download(
        keyword,
        limit=num_images,
        output_dir=output_dir,
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )
    print(f"Downloaded {num_images} images for '{keyword}'")