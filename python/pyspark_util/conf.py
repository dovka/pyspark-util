# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Conf(object):
    @classmethod
    def build(cls, conf=None, **kwargs):
        if conf and kwargs:
            settings = conf.settings()
            settings.update(kwargs)
            return cls(**settings)
        elif conf:
            return conf
        else:
            return cls(**kwargs)

    def settings(self):
        return {k:v for k, v in self.__dict__.items() if v is not None}

    def __str__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join('%s=%s' % (k, v) for k, v in self.settings().items())
        )
