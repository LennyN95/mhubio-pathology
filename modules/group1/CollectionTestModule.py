"""
-------------------------------------------------
MHub - Test Module that runs a third party tool.
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

from mhubio.core import Module, Instance, InstanceDataCollection
from mhubio.core.IO import IO

@IO.ConfigInput('in_datas', 'dicom|nrrd|mha:mod=ct|mr|sm', the="target data that will be converted to nifti")
class CollectionTestModule(Module):

    SCRIPT_PATH = "/app/src/test_collection/dummy_dependency.py"

    @IO.Instance()
    @IO.Inputs('in_datas', the="data to be converted")
    def task(self, instance: Instance, in_datas: InstanceDataCollection) -> None:

        # build command
        bash_command  = [self.SCRIPT_PATH] + [in_data.abspath for in_data in in_datas]

        # execute command
        self.subprocess(bash_command, text=True)