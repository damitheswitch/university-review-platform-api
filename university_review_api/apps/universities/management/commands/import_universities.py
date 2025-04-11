import requests
from django.core.management.base import BaseCommand
from apps.universities.models import University

class Command(BaseCommand):
    help = 'Import universities from the Hipolabs API'
    
    def handle(self, *args, **options):
        url = 'http://universities.hipolabs.com/search'
        
        try:
            # Try with SSL verification disabled due to SSL issues
            response = requests.get(url, verify=False)
            universities_data = response.json()
            
            # Create a set to track unique university names to avoid duplicates
            existing_universities = set(University.objects.values_list('name', 'country').distinct())
            
            universities_to_create = []
            universities_added = 0
            
            for uni_data in universities_data:
                name = uni_data.get('name')
                country = uni_data.get('country')
                website = uni_data.get('web_pages', [None])[0]
                
                # Skip if university with this name and country already exists
                if (name, country) in existing_universities:
                    continue
                
                universities_to_create.append(
                    University(
                        name=name,
                        country=country,
                        website=website
                    )
                )
                existing_universities.add((name, country))
                universities_added += 1
                
                # Batch create every 100 universities
                if len(universities_to_create) >= 100:
                    University.objects.bulk_create(universities_to_create)
                    universities_to_create = []
                    self.stdout.write(f"Added {universities_added} universities so far...")
            
            # Create any remaining universities
            if universities_to_create:
                University.objects.bulk_create(universities_to_create)
            
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {universities_added} universities'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {str(e)}'))
            self.stdout.write(self.style.WARNING('Adding some sample universities instead...'))
            
            # Add some sample universities if the API fails
            sample_universities = [
                {'name': 'Massachusetts Institute of Technology', 'country': 'United States', 'website': 'http://web.mit.edu/'},
                {'name': 'Harvard University', 'country': 'United States', 'website': 'https://www.harvard.edu/'},
                {'name': 'University of Oxford', 'country': 'United Kingdom', 'website': 'http://www.ox.ac.uk/'},
                {'name': 'University of Cambridge', 'country': 'United Kingdom', 'website': 'https://www.cam.ac.uk/'},
                {'name': 'Stanford University', 'country': 'United States', 'website': 'https://www.stanford.edu/'},
                {'name': 'Tsinghua University', 'country': 'China', 'website': 'https://www.tsinghua.edu.cn/'},
                {'name': 'Peking University', 'country': 'China', 'website': 'http://www.pku.edu.cn/'},
                {'name': 'University of Tokyo', 'country': 'Japan', 'website': 'https://www.u-tokyo.ac.jp/'},
                {'name': 'ETH Zurich', 'country': 'Switzerland', 'website': 'https://ethz.ch/'},
                {'name': 'University of Toronto', 'country': 'Canada', 'website': 'https://www.utoronto.ca/'},
            ]
            
            for uni in sample_universities:
                University.objects.get_or_create(
                    name=uni['name'],
                    country=uni['country'],
                    defaults={'website': uni['website']}
                )
            
            self.stdout.write(self.style.SUCCESS(f'Added {len(sample_universities)} sample universities'))