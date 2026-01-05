from download_images import BingBatchDownload

keywords = [
    "birds flying in clear sky",
    "hot air balloons in the sky",
    "paragliders over mountains",
    "kites flying in park",
    "planes in daytime sky",
    "helicopters over city skyline",
    "seagulls flying over ocean",
    "birds flying over forest",
    "bats in night sky",
    "butterflies in open field"
]

for kw in keywords:
    BingBatchDownload(keyword=kw, num_images=17, output_dir='raw_images/negatives')