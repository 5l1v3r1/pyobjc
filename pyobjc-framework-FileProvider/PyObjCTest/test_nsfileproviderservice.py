import FileProvider
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFileProviderService(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            FileProvider.NSFileProviderExtension.supportedServiceSourcesForItemIdentifier_error_,  # noqa: B950
            1,
        )
