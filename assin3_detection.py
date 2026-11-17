import csv
import json
from pathlib import Path

import jetson.inference
import jetson.utils


def main():
    image_dir = Path('/home/nvidia/jetson-inference/data/images')
    output_dir = image_dir / 'test'
    output_dir.mkdir(parents=True, exist_ok=True)
    image_paths = [image_dir / 'image1_bus.jpg', image_dir / 'image2_people.jpg']
    thresholds = [0.3, 0.7]
    records = []
    summaries = []

    for threshold in thresholds:
        net = jetson.inference.detectNet('ssd-mobilenet-v2', threshold=threshold)

        for image_path in image_paths:
            image = jetson.utils.loadImage(str(image_path))
            detections = net.Detect(image, overlay='box,labels,conf')
            output_path = output_dir / f'{image_path.stem}_threshold_{threshold:.1f}.jpg'
            jetson.utils.saveImage(str(output_path), image)

            print(f'\nImage: {image_path.name}')
            print(f'Confidence threshold: {threshold:.1f}')
            print(f'Number of detected objects: {len(detections)}')

            summaries.append({
                'Image': image_path.name,
                'Threshold': threshold,
                'NumberOfDetectedObjects': len(detections)
            })

            for index, detection in enumerate(detections, start=1):
                record = {
                    'Image': image_path.name,
                    'Threshold': threshold,
                    'DetectionID': index,
                    'ClassID': int(detection.ClassID),
                    'ClassName': net.GetClassDesc(detection.ClassID),
                    'Confidence': float(detection.Confidence),
                    'Left': float(detection.Left),
                    'Top': float(detection.Top),
                    'Right': float(detection.Right),
                    'Bottom': float(detection.Bottom),
                    'Width': float(detection.Width),
                    'Height': float(detection.Height),
                    'Area': float(detection.Area),
                    'Center': [float(detection.Center[0]), float(detection.Center[1])]
                }
                records.append(record)
                print(json.dumps(record, ensure_ascii=False, indent=2))

    fields = ['Image', 'Threshold', 'DetectionID', 'ClassID', 'ClassName',
              'Confidence', 'Left', 'Top', 'Right', 'Bottom', 'Width',
              'Height', 'Area', 'Center']

    with (output_dir / 'detections.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            row = dict(record)
            row['Center'] = f"({record['Center'][0]}, {record['Center'][1]})"
            writer.writerow(row)

    with (output_dir / 'summary.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=['Image', 'Threshold', 'NumberOfDetectedObjects'])
        writer.writeheader()
        writer.writerows(summaries)

    (output_dir / 'detections.json').write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8'
    )


if __name__ == '__main__':
    main()
