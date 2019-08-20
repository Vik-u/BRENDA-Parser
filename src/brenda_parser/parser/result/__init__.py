# Copyright 2011-2019 Moritz Emanuel Beber
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


"""
Provide different abstract parsing result classes.

The abstract classes within this sub-package describe the desired shape to be
returned by parser implementations.

"""


from .abstract_id_parsing_result import AbstractIDParsingResult
from .abstract_comment_parsing_result import AbstractCommentParsingResult
from .abstract_entry_parsing_result import AbstractEntryParsingResult
from .abstract_ki_value_parsing_result import AbstractKiValueParsingResult
from .abstract_km_value_parsing_result import AbstractKmValueParsingResult
from .abstract_natural_substrate_product_parsing_result import AbstractNaturalSubstrateProductParsingResult
from .abstract_protein_parsing_result import AbstractProteinParsingResult
from .abstract_reference_parsing_result import AbstractReferenceParsingResult
from .abstract_substrate_product_parsing_result import AbstractSubstrateProductParsingResult
from .abstract_turnover_number_parsing_result import AbstractTurnoverNumberParsingResult
