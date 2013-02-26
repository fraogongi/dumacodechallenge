################################################################################ 
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
################################################################################

from django.db import models

    
class County(models.Model):
    county_name = models.CharField(max_length=80)
    
    def __unicode__(self):
        return self.county_name
        
    
class Ward(models.Model):
    ward_name = models.CharField(max_length=80)
    county = models.ForeignKey(County)
    
    def __unicode__(self):
        return self.ward_name
        
    
class Location(models.Model):
    location_name = models.CharField(max_length=80)
    ward = models.ForeignKey(Ward)
    
    def __unicode__(self):
        return self.location_name
        
        
class Person(models.Model):
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    location = models.ForeignKey(Location, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
