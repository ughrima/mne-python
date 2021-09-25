# Authors: Jeff Hanna <jeff.hanna@gmail.com>
# License: BSD Style.

from functools import partial

from ...utils import verbose
from ..utils import (has_dataset, _data_path_doc, _get_version,
                     _version_doc, _download_mne_dataset)


has_refmeg_noise_data = partial(has_dataset, name='refmeg_noise')


@verbose
def data_path(path=None, force_update=False, update_path=True, download=True,
              verbose=None):  # noqa: D103
    return _download_mne_dataset(
        name='refmeg_noise', processor='unzip', path=path,
        force_update=force_update, update_path=update_path,
        download=download)


data_path.__doc__ = _data_path_doc.format(name='refmeg_noise',
                                          conf='MNE_DATASETS_REFMEG_NOISE_PATH')  # noqa


def get_version():  # noqa: D103
    return _get_version('refmeg_noise')


get_version.__doc__ = _version_doc.format(name='refmeg_noise')
