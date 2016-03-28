from django.test import TestCase
from smart_sa.dashboard.models import Participant


class ParticipantTest(TestCase):
    def setUp(self):
        self.p1 = Participant(
            {
                'patient_id': 'test_patient_1',
                'id_number': '1',
                'gender': 'F',
                'buddy_name': '',
                'initial_referral_alcohol': 0,
                'initial_referral_drug_use': 0,
                'initial_referral_mental_health': 0,
                'initial_referral_other': 0,
                'defaulter': True,
                'defaulter_referral_alcohol': 0,
                'defaulter_referral_drugs': 0,
                'defaulter_referral_mental_health': 0,
                'defaulter_referral_other': 0,
                'counselor_notes': [],
                'session_progress': [],
                'activity_progress': [],
                'game_vars': [],
                u'session_visits': [
                    {u'session': u'Session 1: Session 1: Getting Started',
                     u'timestamp': u'2013-02-12 12:58:17.340000'},
                    {u'session': u'Session 1: Session 1: Getting Started',
                     u'timestamp': u'2013-02-12 13:06:54.064000'}],
                u'activity_visits': [
                    {u'activity': u'Session 1: Activity 1: Session Objectives',
                     u'timestamp': u'2013-02-12 12:58:26.466000'},
                    {u'activity':
                     u'Session 1: Activity 2: Welcome to Masivukeni!',
                     u'timestamp': u'2013-02-12 12:59:26.745000'},
                    {u'activity': u'Session 1: Activity 3: Today',
                     u'timestamp': u'2013-02-12 12:59:40.317000'},
                    {u'activity': u'Session 1: Activity 4: Working Together',
                     u'timestamp': u'2013-02-12 13:00:07.367000'},
                    {u'activity': u'Session 1: Activity 5: What are ARVs',
                     u'timestamp': u'2013-02-12 13:00:19.270000'},
                    {u'activity':
                     u'Session 1: Activity 6: Getting to Know ARVs',
                     u'timestamp': u'2013-02-12 13:00:30.674000'},
                    {u'activity': u'Session 1: Activity 7: Taking ARVs',
                     u'timestamp': u'2013-02-12 13:00:46.991000'},
                    {u'activity': u'Session 1: Activity 7: Taking ARVs',
                     u'timestamp': u'2013-02-12 13:01:09.643000'},
                    {u'activity': u'Session 1: Activity 8: ARV Concerns',
                     u'timestamp': u'2013-02-12 13:01:53.338000'},
                    {u'activity': u'Session 1: Activity 9: How Are You?',
                     u'timestamp': u'2013-02-12 13:02:20.233000'},
                    {u'activity': u'Session 1: Activity 10: Mood Screen',
                     u'timestamp': u'2013-02-12 13:02:35.989000'},
                    {u'activity': u'Session 1: Activity 10: Mood Screen',
                     u'timestamp': u'2013-02-12 13:02:45.988000'},
                    {u'activity': u'Session 1: Activity 11: Alcohol Screen',
                     u'timestamp': u'2013-02-12 13:03:47.628000'},
                    {u'activity': u'Session 1: Activity 11: Alcohol Screen',
                     u'timestamp': u'2013-02-12 13:03:56.598000'},
                    {u'activity': u'Session 1: Activity 12: Drug Screen',
                     u'timestamp': u'2013-02-12 13:04:41.261000'},
                    {u'activity': u'Session 1: Activity 12: Drug Screen',
                     u'timestamp': u'2013-02-12 13:04:47.813000'},
                    {u'activity': u'Session 1: Activity 13: Treatment Support',
                     u'timestamp': u'2013-02-12 13:05:03.694000'},
                    {u'activity': u'Session 1: Activity 13: Treatment Support',
                     u'timestamp': u'2013-02-12 13:05:10.901000'},
                    {u'activity':
                     u'Session 1: Activity 14: Disclosure is Important',
                     u'timestamp': u'2013-02-12 13:05:31.571000'},
                    {u'activity': u'Session 1: Activity 15: Choosing a Buddy',
                     u'timestamp': u'2013-02-12 13:05:40.182000'},
                    {u'activity': u'Session 1: Activity 15: Choosing a Buddy',
                     u'timestamp': u'2013-02-12 13:05:49.808000'},
                    {u'activity':
                     u'Session 1: Activity 16: Next Steps with Buddy',
                     u'timestamp': u'2013-02-12 13:06:03.005000'},
                    {u'activity':
                     u'Session 1: Activity 17: Reasons to Stay Healthy',
                     u'timestamp': u'2013-02-12 13:06:14.206000'},
                    {u'activity':
                     u'Session 1: Activity 17: Reasons to Stay Healthy',
                     u'timestamp': u'2013-02-12 13:06:22.100000'},
                    {u'activity': u'Session 1: Activity 18: End Session',
                     u'timestamp': u'2013-02-12 13:06:32.364000'}],
            })

        self.p2 = Participant({
            u'game_vars': [
                {u'pill_game': u'{"regular": {"pills": [{"color": "#FF0000", \
                "id": "pill_8913", "name": "Efaverinez EFV"}, \
                {"color": "#0000FF", "id": "pill_2044", \
                "name": "Tenofivir TNV"}, {"color": "#00FF00", \
                "id": "pill_9305", "name": "Lamudivine 3TC"}], \
                "day": {"selected": "06:00", "id": "day", \
                "views": [{"top": "105px", "pillId": "pill_8913", \
                "left": "116px"}, {"top": "105px", "pillId": "pill_2044", \
                "left": "62px"}, {"top": "135px", "pillId": "pill_9305", \
                "left": "62px"}]}, "night": {"selected": "na", \
                "id": "night", "views": []}}}'},
                {u'assessmentquiz': u'{"defaulter": {"audit": {"total": 7}, \
                "drugaudit": {"total": 0}, "kten": {"total": 27}}, \
                "regular": {"audit": {}, "kten": {"total": 18}}}'},
                {u'ssnmtree': u'{"defaulter": {"middle1-fruit": \
                {"disclosure": true, "support": true, "name": "person1"}, \
                "bottom1-fruit": {"disclosure": false, "support": false, \
                "name": "person2"}, "bottom2-fruit": {"disclosure": true, \
                "support": true, "name": "person3"}, "top2-fruit": \
                {"disclosure": false, "support": false, "name": "person4"}, \
                "middle4-fruit": {"disclosure": false, "support": true, \
                "name": "person5"}, "middle3-fruit": {"disclosure": true, \
                "support": true, "name": "person6"}}, "regular": \
                {"middle1-fruit": {"disclosure": true, "support": true, \
                "name": "person7"}, "bottom1-fruit": {"disclosure": false, \
                "support": false, "name": "person8"}, "bottom2-fruit": \
                {"disclosure": true, "support": false, "name": "person9"}, \
                "top2-fruit": {"disclosure": false, "support": false, "name": \
                "person10"}, "middle4-fruit": {"disclosure": false, \
                "support": true, "name": "person11"}, "middle3-fruit": \
                {"disclosure": true, "support": true, "name": ""}}}'},
                {u'ssnmtree': u'{"regular": {"middle1-fruit": \
                {"disclosure": true, "support": true, "name": "sizwe"}, \
                "bottom1-fruit": {"disclosure": false, "support": false, \
                "name": "koko"}, "bottom2-fruit": {"disclosure": true, \
                "support": false, "name": "vuvu"}, "top2-fruit": \
                {"disclosure": false, "support": false, "name": "zody"}, \
                "middle4-fruit": {"disclosure": false, "support": false, \
                "name": ""}, "middle3-fruit": {"disclosure": true, \
                "support": true, "name": "lolo"}}}'},
                {u'lifegoals': u'{"regular": {"step4": "educate my self", \
                "step3": "see my kids grow", "step2": "get healtheir", \
                "goal": "buy a car"}}'},
                {u'problemsolving': u'{"defaulter": {"peopletellmenotto": \
                {"customtext": ""}, "forgetful": {"barriers": \
                "tirednesss.confusion", "finalPlan": "setphone as a \
                reminder.speak to dr", "proposals": "get a relative to \
                help you to remember.\\n\\ntreatment buddy,speaking to dr \
                \\n\\n", "archive": [{"barriers": "wheniam drunk \
                iforget to drink my arv`s", "finalPlan": "Before i go to \
                drink i will ask my daughter to remind me my meds when i \
                come backor wake me up if i fall asleep before my next \
                dose.", "proposals": "get a relative to help you to \
                remember."}], "customtext": ""}, "cantgettoclinic": \
                {"customtext": ""}, "angrynurse": {"customtext": ""}, \
                "nonsense": {"customtext": ""}, \
                "confused": {"customtext": ""}, \
                "otherpatients": {"customtext": ""}, \
                "other": {"customtext": ""}, "hopeless": {"customtext": ""}, \
                "notenoughfood": {"customtext": ""}, \
                "feelingill": {"customtext": ""}, \
                "alone": {"barriers": "", "finalPlan": "", "proposals": "", \
                "customtext": ""}, "treatment_fatigue": {"customtext": ""}, \
                "dontwantto": {"customtext": ""}, \
                "happy": {"customtext": ""}}}'}],
        })

    def test_patient_id(self):
        assert self.p1.patient_id() == 'test_patient_1'

    def test_id_number(self):
        assert self.p1.id_number() == '1'

    def test_gender(self):
        assert self.p1.gender() == 'F'

    def test_has_buddy(self):
        assert not self.p1.has_buddy()

    def test_initial_referral_status(self):
        assert self.p1.initial_referral_status() == "-|-|-|-"

    def test_defaulter_status(self):
        self.assertEquals(self.p1.defaulter_status(), "True: -|-|-|-")

    def test_has_counselor_notes(self):
        self.assertEquals(self.p1.has_counselor_notes(), False)

    def test_num_completed_sessions(self):
        self.assertEquals(self.p1.num_completed_sessions(), 0)

    def test_num_incomplete_sessions(self):
        self.assertEquals(self.p1.num_incomplete_sessions(), 0)

    def test_num_completed_activities(self):
        self.assertEquals(self.p1.num_completed_activities(), 0)

    def test_most_recently_completed_session(self):
        self.assertEquals(self.p1.most_recently_completed_session(), None)

    def test_relevant_timestamps(self):
        self.assertEquals(len(self.p1.relevant_timestamps(1)), 27)

    def test_session_duration(self):
        self.assertEquals(self.p1.session_duration(1), 8)

    def test_completed_session_durations(self):
        self.assertEquals(self.p1.completed_session_durations(), "")

    def test_all_session_durations(self):
        self.assertEquals(self.p1.all_session_durations(), "8,0,0,0,0")

    def test_session_45_durations(self):
        self.assertEquals(self.p1.session_45_durations(), "")

    def test_ssnmtree_data(self):
        self.assertEquals(self.p1.ssnmtree_data(), {})

    def test_assessmentquiz_data(self):
        self.assertEquals(self.p1.assessmentquiz_data(), {})

    def test_lifegoals_data(self):
        self.assertEquals(self.p1.lifegoals_data(), {})

    def test_assessmentquiz_scores(self):
        self.assertEquals(self.p2.mood_alcohol_drug_scores(),
                          "18,,")
        self.assertEquals(self.p2.defaulter_mood_alcohol_drug_scores(),
                          "27,7,0")

    def test_ssnmtree_count(self):
        self.assertEquals(self.p1.ssnmtree_total(), 0)
        self.assertEquals(self.p1.ssnmtree_total('defaulter'), 0)
        self.assertEquals(self.p2.ssnmtree_total(), 5)
        self.assertEquals(self.p2.ssnmtree_total('defaulter'), 6)

    def test_ssnmtree_supporters(self):
        self.assertEquals(self.p1.ssnmtree_supporters(), 0)
        self.assertEquals(self.p1.ssnmtree_supporters('defaulter'), 0)
        self.assertEquals(self.p2.ssnmtree_supporters(), 2)
        self.assertEquals(self.p2.ssnmtree_supporters('defaulter'), 4)

    def test_ssnmtree_confidants(self):
        self.assertEquals(self.p1.ssnmtree_confidants(), 0)
        self.assertEquals(self.p1.ssnmtree_confidants('defaulter'), 0)
        self.assertEquals(self.p2.ssnmtree_confidants(), 2)
        self.assertEquals(self.p2.ssnmtree_confidants('defaulter'), 3)

    def test_ssnmtree_supporters_and_confidants(self):
        self.assertEquals(self.p1.ssnmtree_supporters_and_confidants(), 0)
        self.assertEquals(
            self.p1.ssnmtree_supporters_and_confidants('defaulter'), 0)
        self.assertEquals(self.p2.ssnmtree_supporters_and_confidants(), 1)
        self.assertEquals(
            self.p2.ssnmtree_supporters_and_confidants('defaulter'), 3)

    def test_pillgame_list(self):
        self.assertEquals(self.p1.medication_list(), "")
        self.assertEquals(self.p1.defaulter_medication_list(), "")
        self.assertEquals(self.p2.medication_list(),
                          "Efaverinez EFV,Tenofivir TNV,Lamudivine 3TC")
        self.assertEquals(self.p2.defaulter_medication_list(),
                          "")

    def test_barriers(self):
        self.assertEquals(self.p1.barriers(), "")
        self.assertEquals(self.p1.barriers('defaulter'), "")
        self.assertEquals(self.p2.barriers(), "")
        self.assertEquals(self.p2.defaulter_barriers(), "forgetful,alone")
        self.assertEquals(self.p2.defaulter_barriers_with_plans(),
                          "forgetful")
