from django.db import models


class ABACStudent(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    previous_institute = models.CharField(max_length=100)

    def display_gpa(self):
        # Implement your logic here
        pass

    def display_credits_earned(self):
        # Implement your logic here
        pass


class MSMEStudent(models.Model):
    major = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    certificate = models.CharField(max_length=50)

    # Link MSMEStudent to ABACStudent using a ForeignKey
    abac_student = models.ForeignKey(ABACStudent, on_delete=models.CASCADE)

    def display_major(self):
        # Implement your logic here
        pass

    def display_certification(self):
        # Implement your logic here
        pass


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.name
