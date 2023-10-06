from django.db import models


class Relation(models.Model):

    name = models.CharField(max_length=50)


class Candidate(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    relation = models.ForeignKey(
        Relation,
        related_name="relation_for_candidate",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    P = "P"
    S = "S"
    T = "T"

    CANDIDATE_TYPE_CHOICES = [
        (P, "President"),
        (S, "Senator"),
        (T, "Treasurer"),
    ]

    c_type = models.CharField(max_length=1, choices=CANDIDATE_TYPE_CHOICES, default=S)
