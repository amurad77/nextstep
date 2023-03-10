# Generated by Django 4.1.4 on 2022-12-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='First name')),
                ('surname', models.CharField(max_length=256, verbose_name='Last name')),
                ('email', models.EmailField(max_length=60, verbose_name='Your e-mail')),
                ('number', models.CharField(max_length=30, verbose_name='Your Phone')),
                ('what_idea', models.CharField(choices=[('1', 'Select an option'), ('2', 'Early idea'), ('3', 'Researched idea'), ('4', 'Mockups')], default='Select an option', max_length=256, verbose_name='What state is your idea')),
                ('idea', models.CharField(max_length=530, verbose_name='What field is your idea / product / service in?')),
                ('describe', models.TextField(max_length=30000, verbose_name='Describe your startup')),
                ('hours', models.CharField(choices=[('1', 'Select an option'), ('2', '0-10'), ('3', '11-20'), ('4', '21-35'), ('5', '36+')], default='Select an option', max_length=1000, verbose_name='How many hours')),
                ('people', models.CharField(choices=[('1', 'Select an option'), ('2', '1'), ('3', '2'), ('4', '3'), ('5', '4+')], default='Select an option', max_length=1000, verbose_name='How many people')),
                ('more_information', models.TextField(max_length=100, verbose_name='More information about team members')),
                ('industries1', models.CharField(choices=[('1', 'Accouting / Finance / Legal'), ('2', 'Advertising / Marketing'), ('3', 'Agriculture / Farming'), ('4', 'Art / Creative'), ('5', 'Automotive / Transportation'), ('6', 'Biotech / Medical'), ('7', 'Communication / Collaboration / Networking'), ('8', 'Coupons / Deals / Comparison Shopping'), ('9', 'Dating / Relationship'), ('10', 'Digital Media / Content'), ('11', 'E-commerce / Retail'), ('12', 'Education / Edutainment'), ('13', 'Energy / Oil / Gas'), ('14', 'Enterprise Software / Security'), ('15', 'Entrepreneurship / Startups'), ('16', 'Events / Conferences / Concert'), ('17', 'Fashion / Beauty'), ('18', 'Financial Services / Investing'), ('19', 'Food / Restaurant'), ('20', 'Fundraising / Crowdfunding'), ('21', 'Games / Entertainment'), ('22', 'Government / Public Safety'), ('23', 'Greentech / Cleantech / Sustainable'), ('24', 'Hardware / Electronics'), ('25', 'Health / Fitness'), ('26', 'Jobs / Recruiting / Training'), ('27', 'Mental Health / Wellbeing'), ('28', 'Music / Audio'), ('29', 'News / Information'), ('30', 'Nonprofit / Social Services / Donations'), ('31', 'Outsourcing / Services'), ('32', 'Programming / Software Development'), ('33', 'Real Estate'), ('34', 'Pets'), ('35', 'Research / Analytics / Surveys'), ('36', 'Sharing / Rentals / Barter'), ('37', 'Sports'), ('38', 'Travel / Hospitality'), ('39', 'Wines / Alcohol'), ('40', 'Other')], max_length=1000, verbose_name='Two industries that best describe the business you are building (Primary)')),
                ('industries2', models.CharField(choices=[('1', 'Accouting / Finance / Legal'), ('2', 'Advertising / Marketing'), ('3', 'Agriculture / Farming'), ('4', 'Art / Creative'), ('5', 'Automotive / Transportation'), ('6', 'Biotech / Medical'), ('7', 'Communication / Collaboration / Networking'), ('8', 'Coupons / Deals / Comparison Shopping'), ('9', 'Dating / Relationship'), ('10', 'Digital Media / Content'), ('11', 'E-commerce / Retail'), ('12', 'Education / Edutainment'), ('13', 'Energy / Oil / Gas'), ('14', 'Enterprise Software / Security'), ('15', 'Entrepreneurship / Startups'), ('16', 'Events / Conferences / Concert'), ('17', 'Fashion / Beauty'), ('18', 'Financial Services / Investing'), ('19', 'Food / Restaurant'), ('20', 'Fundraising / Crowdfunding'), ('21', 'Games / Entertainment'), ('22', 'Government / Public Safety'), ('23', 'Greentech / Cleantech / Sustainable'), ('24', 'Hardware / Electronics'), ('25', 'Health / Fitness'), ('26', 'Jobs / Recruiting / Training'), ('27', 'Mental Health / Wellbeing'), ('28', 'Music / Audio'), ('29', 'News / Information'), ('30', 'Nonprofit / Social Services / Donations'), ('31', 'Outsourcing / Services'), ('32', 'Programming / Software Development'), ('33', 'Real Estate'), ('34', 'Pets'), ('35', 'Research / Analytics / Surveys'), ('36', 'Sharing / Rentals / Barter'), ('37', 'Sports'), ('38', 'Travel / Hospitality'), ('39', 'Wines / Alcohol'), ('40', 'Other')], max_length=1000, verbose_name='Two industries that best describe the business you are building (Secondary)')),
                ('areas1', models.CharField(choices=[('1', 'Basic entrepreneurial training'), ('2', 'Improving my idea / strategy'), ('3', 'Building a network'), ('4', 'Finding a Co-Founder'), ('5', 'Building a team'), ('6', 'Product development'), ('7', 'Fundraising'), ('8', 'Marketing and Sales'), ('9', 'Internationalisation'), ('10', 'Strategic Partnership')], max_length=1000, verbose_name='Select the two areas where you most need help building a business (Primary)')),
                ('areas2', models.CharField(choices=[('1', 'Basic entrepreneurial training'), ('2', 'Improving my idea / strategy'), ('3', 'Building a network'), ('4', 'Finding a Co-Founder'), ('5', 'Building a team'), ('6', 'Product development'), ('7', 'Fundraising'), ('8', 'Marketing and Sales'), ('9', 'Internationalisation'), ('10', 'Strategic Partnership')], max_length=1000, verbose_name='Select the two areas where you most need help building a business (Secondary)')),
                ('file', models.FileField(upload_to='file', verbose_name='File')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Your Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Your Email')),
                ('number', models.CharField(max_length=20, verbose_name='Your Phone')),
                ('message', models.TextField(max_length=5000, verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
