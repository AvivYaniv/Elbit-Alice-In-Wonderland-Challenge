
class PlayFairCipher:
    def __init__(self, key):
        self.key = key.replace(" ", "").upper()
        result = list()
        for c in self.key:
            if c not in result:
                if c == 'J':
                    result.append('I')
                else:
                    result.append(c)
        flag = 0
        for i in range(65, 91):
            if chr(i) not in result:
                if i == 73 and chr(74) not in result:
                    result.append("I")
                    flag = 1
                elif flag == 0 and i == 73 or i == 74:
                    pass
                else:
                    result.append(chr(i))
        k = 0
        self.matrix = PlayFairCipher.generate_matrix(5, 5, 0)
        for i in range(0, 5):
            for j in range(0, 5):
                self.matrix[i][j] = result[k]
                k += 1

    @staticmethod
    def generate_matrix(x, y, initial):
        return [[initial for _ in range(x)] for _ in range(y)]

    def locindex(self, c):
        loc = list()
        if c == 'J':
            c = 'I'
        for i, j in enumerate(self.matrix):
            for k, l in enumerate(j):
                if c == l:
                    loc.append(i)
                    loc.append(k)
                    return loc

    @staticmethod
    def add_spaces_to_decrypted(encrypted_message, decrypted_message):
        plain_with_spaces   = [''] * len(encrypted_message)
        decrypted_iterator  = iter(decrypted_message)
        for i, e in enumerate(encrypted_message):
            if ' ' == e:
                plain_with_spaces[i] = ' '
            else:
                plain_with_spaces[i] = decrypted_iterator.next()
        return ''.join(plain_with_spaces)

    def decrypt(self, encrypted_message):
        decrypted_message   = ''
        message_to_decrypt  = encrypted_message.replace(" ", "").upper()
        i = 0
        while i < len(message_to_decrypt):
            loc  = list()
            loc  = self.locindex(message_to_decrypt[i])
            loc1 = list()
            loc1 = self.locindex(message_to_decrypt[i + 1])
            if loc[1] == loc1[1]:
                decrypted_message += "{}{}".format(self.matrix[(loc[0] - 1) % 5][loc[1]],  self.matrix[(loc1[0] - 1) % 5][loc1[1]])
            elif loc[0] == loc1[0]:
                decrypted_message += "{}{}".format(self.matrix[loc[0]][(loc[1] - 1) % 5],  self.matrix[loc1[0]][(loc1[1] - 1) % 5])
            else:
                decrypted_message += "{}{}".format(self.matrix[loc[0]][loc1[1]],           self.matrix[loc1[0]][loc[1]])
            i = i + 2
        return PlayFairCipher.add_spaces_to_decrypted(encrypted_message, decrypted_message)

play_fair_cipher    = PlayFairCipher(key = 'alice')
encrypted_message   = 'Ugl ubkfaugmcl zipu tuslchby tm iana l uqttai gns tpnl zcv ikg rphm fenuhf rrhhlmiw gmys xn trhhlmic ybeq Cicea bef mty l kpnipz zt yfeom bkptu tytqqfsh bluuiid hagnul ufi hptmf phstaio oliicof gmxm b aluw gbbm zaiiAcsphs uph zlff vlq xluw gbbk ps tph hiff zatw rimycw gns tph beh miaosc tg slna ly yph zlos gmxm yt cmpm bkptu glu ikg rm ypohlw lber yiq otfso yp gekuht tizs Glstu ufc usllh yt cmpm gmxm ikm rbqc pqu zdcq ufl ziq gtnlof yt hqs cr yiq ytm glqo qn tbb ikcyfeof ugip ufa iuupab lz zph xfhlt ng sph zlff ikf mtycelh ugcq ugcz zlul nffflh xlug etkhkcwmq imf gkpmufaizau flua lmf uglui uph qil rekq imf negyqsiu pzof zupo uhft Ufc uuum bmyk i cls dtmn ppi ng ugi uphawiu iq ufh uiquif lr yiq ilhafflh MTIKHC KLWRLILBA hqu yt pht dulcq flqiqqncosplos cs vlu inkyc ufl hlf opr canc um gtmo uph cls dmt hilq ng nafffsf tpnahmgx tp nikcblh yt uzs cs cosu upi ng uga ezugklqfr iq ufi haie miqs crYaic rgpthgu Licec up gluuiid ibucs tteb e biff iq ugfx F xbeff ugfsm otyfeof ng uqkdicof gmxm tulcst Gpv dqlza ugczff lic rfeom pl cq gppl Zdx C ymrefmu tcv ikcyfeof bkpts cu czas fn F hiff ngg sph ytk pg sph gpqtl Zfeeg vlq xluw canaic ysqlHmym fmym fmym Xptdm ugi hlii mazlu gtpl yt ik ipf L ymmflu gpl rikw ociiu Axi hliiak fc yfet ulni uph qilf liptf L prtu ha hczzfsf tpnlzphul pilq uga eipusc pg sph alsud Ecu pl uic uber yptdm ha gnqs ugptqimf nliar fmys F ugfsn bmt ctq tbb Liceh plb ialqos uizaqlc rfeoft ng sfey ymts cp flu iayypox fo sph tigpmctmpn ikg rgpthg ufer xiq opq c zatw otmg pkkpsuspcsx gmt ufmyfso too phq mopldlhhc iq uglul ziq op poc um cfxuco sp glu tucii cr yiq otmg mulescea yt qix cy tzat wiu ugcqq igkqu ugl ucfgu fltuikeahqz zphs F ymmflu zdcq Ilscuqhl mt Cmofcsrha Cza otz zk Cicea bef mn chll vber Ccqcsrhl ziq mt Cmofcsrhb bcsphq dqu ugpthbz zphz xlui pcec hqlmf ymwmt un tcvMuiuiprcx tph habck ibcfs L xpohls ln F uflii dlid wcfgu ugtmthg uph alsuk Kmy hsttx crci rbbo rt gpnc pqu lkpoo yph uhpkia ugcq vlam xlug ugacu dalfr gmxmvlwm Uga Losencqfeiu C sfeom ufl ziq qluglu dclb uglul ziq op poa ifxucsfof ugfx scpl iq cs flfmu tptmf cq lic rph slhbr ymtf dqu F xbeff beza yt iqo qphr lbez zph kipl ng uga eptostw fx ctq popz Miaiql Pddn lt ufex Slz Ehliikg mq Lqtuslicl ikf rph uscag rt gqsutcz iq ufi ukppabioic gqsutczfsb ct xptul bifffso ydupthb uga lls Gm ctq ufeom ctt eptdm klkihc cs Ikm lbeq cs ffomtikr ccsrcc hlsi rphff ugfsm ni hmt iqnaof Op csff pizaw mt yk cqn uhudekx F uflii rbb cs lwcsucp sn upnlzphulGmxm gmxm gmxm Uglul ziq opugfsh circ um gn tk Cicea tnpo habco slinaof cblcm Ffsebff nlyy pl zatw preg ytsfhbs C ufptdm ugfsm Bfseb vlt uph els C gpuh ugczff ulplkdlu phs teqeat md nciq bz zalscpl Flkid pw gals L xluf ctr zlul hmyp flul zcsd pc Uphul lqi pp ncea co sph lcs Lk ldslcf dqu ctr pcfgu elygb e kbq cmf ugcqq xluw cana l npqtc zpt momy Hqr gt gcqu icq kbut L xpohlq Lmf phul Licea hchik yt hcu scqphs tiahuv cmf zlos po qixcof yt phstain fk i mwalow tnsu ng vlw Gt gcqu icq kbut Gm elut alq gcqq imf tnplscplr Fk gcqu icq elut gnt wpt uia ly yph gtrefmq csxzlu lcsphs rzhtucns fr glfos preg klzzlu zdced zcv ufh uqu cs Ufi haiz zbeu tph vlr fpyfso too ikf blb estu hahto sm gullk ugcq ufl ziq vlamfsh bikf lp fikm lcsb Ffseb ikf rcvfso yp glu zatw alsmiurcx Omy Flkig uaid rc uph usqub flf ctz hzau lcq b kcq zdip tqnnipcw ugrpo upznk gmxm ufa elkh zkpk i phek ng tucenq ikn ntw iabaiu ikg rph biff vlt nzaqLicea vlx sty b kcs pzsu ikf rph esnklh zu po yt phs dbbs ck i npplos ufa iuupah rk hqu cs vlq iff blqm kyluphlb hagnul phw liq iktyphw dpoh oiqqihc ikg rph Zdcsl Ubkfar yiq tucii cs xcfgu pzxxxcof gmxm cs Uglul ziq opq c npplos yt ha cmtu lvcv zlos Licea ianc uph xlmf ikm liq estu fs scpl yt phlq cs qiv cx fz zqspib l gtsmlu Pg ow alst ikm lfeqnluu fmy iluc cst fcuscof Ufl ziq einta hhpfsf lr yphs xph uqsmlh uga emtpiq dqu ugl Ubkfar yiq op cmoflu yt ha uiip ufi hptmf phstain fk i cmof cmz dlid lfeeg vlr ics zu gv l qmy ng ilnku fikfcof dspn ugl uuugSphul zlul gmmtq iff tmspg rph beff hqz zphz xlua lff cmaolh ikm lphk Iicea bef dbbk iff ugl zcv gmxm poi ulfa lmf zu ugc puglu usxcof azluw guus tph vlamlh qimdw gmyo sph nlnnia ymmflufsh bmy ufl ziq azlu yt hcy tqu cblcsXrhhlmix tph elpl zupo l icsrcc udubbiapplh qcdaa lff klhl ng tnicf hilyy uglul ziq opugfso ts fu cyihuq c scox otdmip pav cmf Liceiu nfstz zgpthgu vlt ubes cr ocfgu hacmof yt poc pg sph gmmtt ng sph beff hqq cilu icsphs uph cmaor xluc uuu iltdc ps uph paz xiq ytn tklff hqq cq cox qluc cs ymref mty pkip ikc tg sphp Dmyazlu po ugi uaepog rlnl uptmf ufa elkh zkpk i cmy lqsqcfs ufh plb ops otycelh hagnul ikf dhpfsf lr yiq l icsrcl huuq lgkqu nfgsbbs foiphu fcff uph uscag rph iczzia otdmip pax co sph cmao ikg rp glu dtalr gaicfgu cs nfzzlh'
# THE RABBITHOLE WENT STRAIGHT ON LIKE A TUOOEL FOR SOME WAY AND THEN DIPPED SUDDENLY DOWN SO SUDDENLY THAT ALICE HAD NOT A MOMENU UO THINK ABOUT STOKKING HERSELF BEFORE SHE FOUND HERSELG GALLING DOWN A VERY DAAP WELLEITHER THE WEII WAS VERY DAAP OR SHE FEII VERY SLOWLY FOR SHE HAD PLENTY OF TIME AT THE WENT DOWN TO LOOK ABOUT HER AND TO WONDER WHAT WAS GOING TO HAPPEO OEXT FIRST SHE TRIED TO LOOK DOWN AND MAKE OUT WHAT SHE WAS COMING TO BUT IT WAS TOO DARK TO SAA ANYTHING THEN SHE LPPKED AU UHE SIDES OF THE WEII AND NOTICED THAT THEY WERE FIIIED WITH CUPBOARDS AND BOOKSHELVES HERE AND THERE SHE SAW MAPS AND PICTURES HUNG UPON PEGS SHE TPPK DOWN A IAR FROM ONE OF THE SHELVES AS SHE PASSED IT WAS LABEIIED ORANGE MARMALADE BUT TO HER GREAT DISAKKOINTMENT IT WAS EMPTY SHE DID NOT LIKE TO DROP THE IAR FOR FEAR OF KIIIING SOMEBODY SO MANAGED TO PUT IT INTP PNE OF THE CUPBOARDS AS SHE FELL PAST ITWELL THOUGHT ALICE TO HERSELF AFTER SUCH A FAII AS THIS I SHAII THINK NOTHING OF TUMBLING DOWN STAIRS HOW BRAVE THEYII ALL THINK ME AT HOME WHY I WOULDNT SAY ANYTHING ABOUT IT EVEN IF I FEII OFF THE TOP OF THE HOUSE WHICH WAS VERY LIKELY TRUEDOWN DOWN DOWN WOULD THE FALL NEVER COME TO AN END I WONDER HOW MANY MILES IVE FALLEN BY THIS TIME SHE SAID ALOUD I MUST BE GEUUING SOMEWHERE NEAR THE CENTRE OF THE EARTH LET ME SEE THAT WOULD BE FOUR THOUSAND MILES DOWN I THINK FOR YOU SAA ALICE HAD LEARNT SEVERAL THINGS OF THIT TORT IN HER LETTONS IN THE SCHOOLROOM AND THOUGH THIS WAS NOT A VERY GOOD OPPORTUNITY FOR SHOWING OGG HER KNOWLEDGE AS THERE WAS NO ONE TO LISTEN TO HER STILL IT WAS GOOD PRACTICE TO SAY IT OVER YES THATS ABOUT THE RIGHT DISTANCEBUU UHEN I WONDER WHAT LATITUDE OR LONGITUDE IVE GOU UO ALICE HAD NO IDEA WHAT LATITUDE WAS OR LONGITUDA AITHER BUT THOUGHU UHEY WERE NICE GRAND WORDS TO SAYPRESENTLY SHE BEGAN AGAIN I WONDER IF I SHALL FALL RIGHT THROUGH THE EARTB BOW FUOOY ITLL SAAM TO COME OUT AMONG THE PEOPLE THAT WALK WITH THEIR HEADS DOWNWARD THE ANTIPATHIES I THINK SHE WAS RATHER GLAD THERE WAS NO ONE LISTENING THIS TIME AS IT DIDNT SOUND AT ALL THE RIGHT WORD BUT I SHAII HAVE TO ASK THEM WHAU UHE NAME OF THE COUNTRY IS YOU KNOW PLEASE MLLM IS THIS NEW ZEALAND OR AUSTRALIA AND SHE TRIED TO CURTSEY AS SHE SPOKEFANCY CURTSEYING AS YOURE FAIIING THROUGH THE AIR DO YOU THINK YOU COULD MANAGE IT AND WHAT AN IGNORANT LITTLE GIRL SHEII THINK ME FOR ASKING NO ITII NEVER DO TO ASK PERHAPS I SHALL SAA IT WRITTEN UP SOMEWHEREDOWN DOWN DOWN THERE WAS NOTHING ELSE TO DO SO ALICE SOON BEGAN TALKING AGAIN DINAHII MITT ME VERY MUCH TONIGHT I SHOULD THINK DINAH WAS THE CAT I HOPE THEYII REMEMBER HER SAUCER OF MILK AU UEATIME DINAH MY DEAR I WISH YOU WERE DOWN HERE WITH ME THERE ARE NO MICE IN THE AIR IM AFRAID BUT YOU MIGHT CATCH A BAT AND THATS VERY LIKE A MOUSE YOU KNOW BUT DO CATS EAT BATS I WONDER AND HERE ALICE BEGAN TO GET RATHER SLEEPY AND WENT ON SAYING TO HERSELF IN A DREAMY SORT OF WAY DO CATS EAT BATS DO CATS EAT BATS AND SOMETIMES DO BATS EAT CATS FOR YOU SEE AT THE COULDNT ANSWER EITHER QUESTION IT DIDNT MUCH MAUUER WHICH WAY SHE PUT IT SHE FELU UHAT SHE WAS DOZING OGG AND HAD IUST BEGUN TO DREAM THAT SHE WAS WALKING HAND IN HAND WITH DINAH AND SAYING TO HER VERY EARNESTLY NOW DINAH TELL ME THE TRUTH DID YOU EVER EAT A BAT WHEN SUFFENLY THUMP THUMP DOWN SHE CAME UPON A HEAP OF STICKS ANF FRY LEAVES AND THE FAII WAS OVERALICE WAS NOT A BIT HURT AND SHE IUMPED UP ON TO HER FAAT IN A MOMENT SHE LPPKED UP BUT IT WAS AII DARK OVERHEAD BEFORE HER WAS ANOTHER LONG PASSAGE AND THE WHITE RABBIT WAS STILL IN SIGHT HUSSYING DOWN IT THERE WAS NOT A MOMENT TO BE LOST AWAY WENT ALICE LIKE THE WIND AND WAS IUST IN TIME TO HEAR IT SAY AS IU UURNED A CORNER OH MY EARS AND WHISKERS HOW LATE ITS GETTING SHE WAS CLOSE BEHIND IT WHEN SHE TURNED THE CORNER BUT THE RABBIT WAS NO LONGER TO BE SEEN SHE FOUND HERSELF IN A LONG LOW HALL WHICH WAS LIT UP BY A ROW OF LAMPS HANGING FROM THE RPPFTHERE WERE DOORS AII ROUND THE HAII BUU UHEY WERE AII LOCKED AND WHEN ALICE HAD BAAN AII THE WAY DOWN ONE SIDE AND UP THE OTHER TRYING EVERY DPPR SHE WALKED SADLY DOWN THE MIFFLE WONDERING HOW SHE WAS EVER TO GET OUT AGAINSUDDENLY SHE CAME UPON A LITTLE THRAALEHHED TABLE AII MADE OF SOLID GLATT THERE WAS NOTHING ON IT EXCEPT A TINY GOLDEN KEY AND ALICES FIRSU UHOUGHT WAS THAT IT MIGHT BELONG TO ONE OF THE DOORS OF THE HAII BUT ALAS EITHER THE LOCKS WERE TPP LARGE OR THE KEY WAS TOO SMAII BUT AT ANY RATE IT WOULD NOT OPEN ANY OF THEM HOWEVER ON THE SECOND TIME ROUND SHE CAME UPON A LOW CURTAIN SHE HAD NOT NOTICED BEFORE AND BEHIND IT WAS A LITTLE DPPR ABOUT FIFTAAN INCHES HIGH SHE TRIED THE LIUULE GOLDEN KEY IN THE LOCK AND TO HER GREAT DELIGHT IT FIUUED
print(play_fair_cipher.decrypt(encrypted_message))
