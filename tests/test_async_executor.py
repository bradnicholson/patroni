import unittest

from mock import Mock, patch
from patroni.async_executor import AsyncExecutor, CriticalTask
from threading import Thread


class TestAsyncExecutor(unittest.TestCase):

    def setUp(self):
        self.a = AsyncExecutor(Mock())

    @patch.object(Thread, 'start', Mock())
    def test_run_async(self):
        self.a.run_async(Mock(return_value=True))

    def test_run(self):
        self.a.run(Mock(side_effect=Exception()))


class TestCriticalTask(unittest.TestCase):

    def test_completed_task(self):
        ct = CriticalTask()
        ct.complete(1)
        self.assertFalse(ct.cancel())
