import logging

def apply_patch(dataset_metadata: dict, patch_data: dict):
    '''For each key in patch_data, apply its value to dataset_metadata.'''
    for key, value in patch_data.items():
        logging.info(f" apply_patch - {key}: {value}")
        dataset_metadata[key] = value
    return dataset_metadata


def set_date_updated(dataset_metadata: dict, date_updated: str):
    '''Set the `date_updated` field of `dataset_metadata`.'''
    logging.info(f" setting `date_updated` to {date_updated}")
    dataset_metadata['date_updated'] = date_updated
    return dataset_metadata
