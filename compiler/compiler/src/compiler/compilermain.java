package compiler;

import java.io.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class compilermain {
	private String[] kernel = new String[500];
	private int kerind = 0;
	private String[] rule = new String[500];
	private String[] Lrule = new String[500]; // 왼쪽룰
	private String[] Rrulr = new String[500]; // 오른쪽 룰
	private String[] NT = new String[500]; // 논터미널 기호 집합
	private String[] TM = new String[1000]; // 터미널 기호 집합
	private String[][] first = new String[500][100];		//first집합
	private String[][] fallow = new String[500][100];		//팔로우집합
	private String[][] canset = new String[500][100];		//정규항목집합
	private String[][] ActionTable;
	private String[][] GotoTable;
	private int canind[] = new int[500];					
	private int colind = 0;						
	private boolean nullable[] = new boolean[500];
	private int firstind[] = new int[500];
	private int fallowind[] = new int[500];
	private int rulrIdx = 0; // 룰 인덱스
	private int tmind = 0; // 터미널심볼 인덱스
	private int ntind = 0; // 논터미널심볼 인덱스
	private int i = 0;
	private Stack<String> stack = new Stack<>();
	String input;
	int cur_input_ptr = 0;
	private int[][] powerset = new int[500][500];
	private int[] psind1 = new int[500];
	private int psind2 = 0;
	String tree[] = new String[500];
	private int treeind = 0;
	private String[][] lookahead;
	private int lahind1[];
	private int lahind2=0;
	
	public Queue<String> setlah(int state,int cannum,String can,Queue<Integer> predd)
	{
		Queue<String> result = new LinkedList<String>();
		Queue<Integer> prd = new LinkedList<Integer>();
		
		if(canset[state][cannum].split(" ==> ")[0].equals("S'"))
		{
			result.offer("$");
			return result;
		}
		int cannum2=0;
		int wd = 0;
		for(int i=0 ; i<canset[state][cannum].split(" ").length ; i++)
		{
			if(canset[state][cannum].split(" ")[i].equals("."))
			{
				wd = i;
				break;
			}
		}
		wd -=2;
		
			prd = pred(wd,state);
		int af[] = new int[prd.size()];
		int afind=0;
		if(prd.contains(state))
		{
			while(true)
			{
				if(prd.isEmpty())
					break;
				int bgbg = prd.poll();
				if(bgbg != state)
				{
					af[afind] = bgbg;
					afind++;
				}
				else
				{
				}
			}
		}
		for(int i=0 ; i<afind ; i++)
			if(predd.contains((af[i])))
				af[i] = -99;
		for(int i=0 ; i<=afind-1 ; i++)
		{
			if(af[i] != -99)
				prd.offer(af[i]);
		}
		int wheredot = 0;
		while(!prd.isEmpty())
		{
			int a = prd.poll();
			int can2ind=0;
			String can3[] = new String[100];
			

			String tmp = can.split(" ==> ")[0];
			for(int j=canind[a]-1 ; j>=0 ; j--)
			{
				if(canset[a][j].charAt(canset[a][j].length()-1) == '.')
				{
					continue;
				}
				if(canset[a][j].split("[.]")[1].trim().contains(" "))
				{
					if(canset[a][j].split(" ==> ")[0].equals(tmp))
						continue;
					if(canset[a][j].split("[.]")[1].trim().split(" ")[0].equals(tmp))
					{
						boolean fafa=false;
						for(int xi = 0 ; xi<can2ind ; xi++)
						{
							if(can3[xi].equals(canset[a][j]))
							{
								fafa=true;
								break;
							}
						}
						if(fafa)
							continue;
						can3[can2ind] = canset[a][j];
						can2ind++;;
					}
				}
				else if(canset[a][j].split("[.]")[1].trim().equals(tmp))
				{
					if(canset[a][j].split(" ==> ")[0].equals(tmp))
						continue;
					boolean fafa=false;
					for(int xi = 0 ; xi<can2ind ; xi++)
					{
						if(can3[xi].equals(canset[a][j]))
						{
							fafa=true;
							break;
						}
					}
					if(fafa)
						continue;
					can3[can2ind] = canset[a][j];
					can2ind++;
				}
			}
			for(int xb=0 ; xb<can2ind ; xb++)
			{
				String can2 = can3[xb];

				for(int i=canind[a]-1 ; i>=0 ; i--)
				{
					if(canset[a][i].replace(" .","").equals(can2.replace(" .", "")))
					{
						if(canset[a][i].contains("S'"))
						{
							result.offer("$");
							break;
						}
							
						for(int j=0 ; j<can2.split(" ").length ; j++)
						{
							if(can2.split(" ")[j].equals("."))
							{
								wheredot = j;
								break;
							}
						}
						if(wheredot>can2.split(" ").length-3)
						{
							
						}
						else
						{
							String tmp1 = can2.split(" ")[wheredot+2];
							int[] ntnt = checknt(tmp1);
							if(ntnt[0] == 1)
							{
								for(int j=0 ; j<firstind[ntnt[1]] ; j++)
								{
									result.offer(first[ntnt[1]][j]);
								}
							}
							else
							{
								result.offer(tmp1);
							}
						}
						
						if(wheredot>2)
						{
							predd.offer(state);
							Queue<String> fftmp = setlah(a,i,canset[a][i],predd);
							result.addAll(fftmp);
						}
						else
						{
							if(i==0)
							{
								continue;
							}
							String tmp1 = can2.split(" ==> ")[0];
							for(int j=i-1 ; j>=0 ; j--)
							{
								//if(canset[a][j].equals(can2))
									//continue;
								if(canset[a][j].split("[.]")[1].trim().contains(" "))
								{
									if(canset[a][j].split("[.]")[1].trim().split(" ")[0].equals(tmp1))
									{
										can2 = canset[a][j];
										break;
									}
								}
								else if(canset[a][j].split("[.]")[1].trim().equals(tmp1))
								{
									can2 = canset[a][j];
									break;
								}
							}
							
						}
					}
					else
						continue;
				}
			}
		}
		
		/*
		if(canset[state][cannum].split(" ==> ")[0].equals("S'"))
		{
			result.offer("$");
		}
		else
		{
			prd = pred(state,cannum);
			
		}*/
		return result;
	}
	
	public void lahset()
	{
		Queue<Integer> lqu = new LinkedList<Integer>();
		Queue<Integer> lqu2 = new LinkedList<Integer>();
		Queue<String> lqu3 = new LinkedList<String>();
		Queue<String> result;
		int wheredot = 0;
		String abc;
		for(int i=0 ; i<colind ; i++)
		{
			for(int j=0 ; j<canind[i] ; j++)
			{
				abc = canset[i][j];
				for(int x=0 ; x<abc.split(" ").length ; x++)
				{
					if(abc.split(" ")[x].equals("."))
					{
						wheredot = x;
						break;
					}
				}
				if(wheredot == abc.split(" ").length - 1 )
				{
					lqu.offer(i);
					lqu2.offer(j);
					//lqu3.offer(abc.replace(" .", ""));
					lqu3.offer(abc);
					continue;
				}
			}
		}
		while(!lqu.isEmpty())
		{
			int a = lqu.poll();
			int b = lqu2.poll();
			String r = lqu3.poll();
			String tmp = new String(r);
			
			Queue<Integer> predd = new LinkedList<Integer>();
			predd.offer(a);
			result = setlah(a,b,r,predd);
			
			String c = null;
			while(!result.isEmpty())
			{
				int[] ntnt = new int[2];
				int gg = 0;
				c = result.poll();
				ntnt = checknt(c);
				for(int i=0 ; i<rulrIdx ; i++)
				{
					if(rule[i].equals(tmp.replace(" .", "")))
					{
						gg = i;
						break;
					}
				}
				if(gg==0)
					ActionTable[a][ntnt[1]] = "Acc";
				if(!"Acc".equals(ActionTable[a][ntnt[1]]) && ActionTable[a][ntnt[1]] == null)
					ActionTable[a][ntnt[1]] = "r"+gg;
			}
		}
	}
	
	public Queue<String> ringsum(Queue<String> a, Queue<String> b)
	{
		Queue<String> result = new LinkedList<String>();
		if(a.contains("__"))
		{
			while(!a.isEmpty())
			{
				String c = a.poll();
				if(c.equals("__"))
					continue;
				else if(result.contains(c))
					continue;
				else
					result.offer(c);
			}
			while(!b.isEmpty())
			{
				String c = b.poll();
				if(result.contains(c))
					continue;
				else
					result.offer(c);
			}
		}
		else
		{
			while(!a.isEmpty())
			{
				String c = a.poll();
				if(result.contains(c))
					continue;
				else
					result.offer(a.poll());
			}
		}
		return result;
	}
	
	public Queue<Integer> pred(int pos,int x)
	{

		boolean gg = false;
		Queue<Integer> que = new LinkedList<Integer>();
		int g;
		que.offer(x);
		int ggg=1;
		while(ggg>0)
		{
			g = que.poll();
			ggg--;
			for(int i=0 ; i<colind ; i++)
			{
				gg=false;
				for(int j=0 ; j<ntind ; j++)
				{
					if(GotoTable[i][j] == null)
						continue;
					if(Integer.parseInt(String.valueOf(GotoTable[i][j].replace("q", ""))) == g)
					{
						que.offer(i);
						if(pos>1)
							ggg++;
						gg=true;
						break;
					}
				}
				if(gg)
					continue;
				for(int j=1 ; j<tmind ; j++)
				{
					if(ActionTable[i][j] == null)
						continue;
					if(ActionTable[i][j].charAt(0) == 'r')
							continue;
					if(Integer.parseInt(String.valueOf(ActionTable[i][j].replace("s", ""))) == g)
					{
						que.offer(i);
						if(pos>1)
							ggg++;
						break;
					}
				}
			}
			pos--;
		}
		
		return que;
		
	}
	
	public void rmfl()
	{
		for(int i=0 ; i<ntind ; i++)
		{
			for(int j=0 ; j<firstind[i] ; j++)
			{
				if(first[i][j].equals("__"))
				{
					boolean f=false;
					for(int x=j ; j<firstind[i] ; j++)
					{
						first[i][x] = first[i][x+1];
						first[i][x+1] = null;
						f=true;
					}
					if(f)
						firstind[i]--;
				}
			}
		}
	}
	
	public static void run1() throws IOException		//
	{
		
		
		compilermain cm = new compilermain();
		
		boolean b;
		try {
			b = cm.RMF("C:\\Users\\강민수\\Documents\\새 폴더\\grammer.txt");
			if (!b) {
				System.out.println("RMF(문법파일 읽기 및 룰 추출 등)에 실패했습니다");
				return;
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		for (cm.i = 0; cm.i < cm.ntind; cm.i++) {
			System.out.println("NT symbol : " + cm.NT[cm.i]);
		}
		cm.FT();
		for (cm.i = 0; cm.i < cm.tmind; cm.i++) {
			System.out.println("TM symbol : " + cm.TM[cm.i]);
		}
		System.out.println("터미널 갯수 : " + cm.tmind + "\t 논터미널 갯수 : " + cm.ntind);
		cm.findFirst();
		for (int j = 0; j < cm.ntind; j++) {
			System.out.print(cm.NT[j] + "'s first : ");
			for (int k = 0; k < cm.firstind[j]; k++) {
				if (k == cm.firstind[j] - 1)
					System.out.print(cm.first[j][k]);
				else
					System.out.print(cm.first[j][k] + ",");
			}
			System.out.print("\n");
		}
		
		cm.findnullable();
		cm.removenullable();
		cm.rmfl();
		cm.findFallow();
		System.out.println("-------------------------------------------------------");
		System.out.println("엡실론 변환 규칙을 제거한 후 문법 : (엡실론 변환 규칙이 없을 경우 동일함)");
		for(int i=0 ; i<cm.rulrIdx ; i++)
		{
			System.out.println("L : "+cm.Lrule[i]+" R : "+cm.Rrulr[i]);
		}
		
		for (int j = 0; j < cm.ntind; j++) {
			System.out.print(cm.NT[j] + "'s fallow : ");
			for (int k = 0; k < cm.fallowind[j]; k++) {
				if (k == cm.fallowind[j] - 1)
					System.out.print(cm.fallow[j][k]);
				else
					System.out.print(cm.fallow[j][k] + ",");
			}
			System.out.print("\n");
		}
		
		
		cm.CreateTable();
		cm.canonicalset();
		//cm.canonicalsetCLR();
		cm.removereduce();
		cm.lahset();
		for(int j=0 ; j<cm.colind ; j++)
		{
			System.out.println(j+"번 정규항목집합 : ");
			for(int i=0 ; i<cm.canind[j] ; i++)
			{
				System.out.println(cm.canset[j][i]);
			}
		}
		
		
		System.out.println("---------------------------------------------------------------------------------------------------");
		System.out.print("|       |");
		for(int i=1 ; i<cm.ntind ; i++)
			System.out.print(String.format("%5s",cm.NT[i])+String.format("%5s", "|"));
		for(int i=0 ; i<cm.tmind ; i++)
			System.out.print(String.format("%5s", cm.TM[i])+String.format("%5s", "|"));
		System.out.println("");
		for(int i=0 ; i<cm.colind ; i++)
		{
			System.out.println("---------------------------------------------------------------------------------------------------");
			System.out.print("|"+String.format("%4d", i)+String.format("%4s", "|"));
			for(int j=1 ; j<cm.ntind ; j++)
			{
					if(cm.GotoTable[i][j] !=  null)
						System.out.print(String.format("%5s", cm.GotoTable[i][j])+String.format("%5s","|"));
					else
						System.out.print(String.format("%10s", "|"));
			}
			for(int j=0 ; j<cm.tmind ; j++)
			{
				int tmp = j;
				if(tmp == cm.tmind)
					continue;
				if(cm.ActionTable[i][tmp] != null)
					System.out.print(String.format("%5s", cm.ActionTable[i][tmp])+String.format("%5s","|"));
				else
					System.out.print(String.format("%10s", "|"));
			}
			System.out.println("");
		}
		System.out.println("---------------------------------------------------------------------------------------------------");
		
		
		
		cm.saveComponent();
		
		cm.SLR();
		
	}
	public static void run2() throws IOException
	{
		compilermain cm = new compilermain();
		cm.readComponentAndSLR();
		

		for (cm.i = 0; cm.i < cm.ntind; cm.i++) {
			System.out.println("NT symbol : " + cm.NT[cm.i]);
		}
		for (cm.i = 0; cm.i < cm.tmind; cm.i++) {
			System.out.println("TM symbol : " + cm.TM[cm.i]);
		}
		System.out.println("터미널 갯수 : " + cm.tmind + "\t 논터미널 갯수 : " + cm.ntind);
		System.out.println("-------------------------------------------------------");
		System.out.println("엡실론 변환 규칙을 제거한 후 문법 : (엡실론 변환 규칙이 없을 경우 동일함)");
		for(int i=0 ; i<cm.rulrIdx ; i++)
		{
			System.out.println("L : "+cm.Lrule[i]+" R : "+cm.Rrulr[i]);
		}
		for (int j = 0; j < cm.ntind; j++) {
			System.out.print(cm.NT[j] + "'s fallow : ");
			for (int k = 0; k < cm.fallowind[j]; k++) {
				if (k == cm.fallowind[j] - 1)
					System.out.print(cm.fallow[j][k]);
				else
					System.out.print(cm.fallow[j][k] + ",");
			}
			System.out.print("\n");
		}
		for(int j=0 ; j<cm.colind ; j++)
		{
			System.out.println(j+"번 정규항목집합 : ");
			for(int i=0 ; i<cm.canind[j] ; i++)
			{
				System.out.println(cm.canset[j][i]);
			}
		}
		
		System.out.println("---------------------------------------------------------------------------------------------------");
		System.out.print("|       |");
		for(int i=1 ; i<cm.ntind ; i++)
			System.out.print(String.format("%5s",cm.NT[i])+String.format("%5s", "|"));
		for(int i=0 ; i<cm.tmind ; i++)
			System.out.print(String.format("%5s", cm.TM[i])+String.format("%5s", "|"));
		System.out.println("");
		for(int i=0 ; i<cm.colind ; i++)
		{
			System.out.println("---------------------------------------------------------------------------------------------------");
			System.out.print("|"+String.format("%4d", i)+String.format("%4s", "|"));
			for(int j=1 ; j<cm.ntind ; j++)
			{
					if(cm.GotoTable[i][j] !=  null)
						System.out.print(String.format("%5s", cm.GotoTable[i][j])+String.format("%5s","|"));
					else
						System.out.print(String.format("%10s", "|"));
			}
			for(int j=0 ; j<cm.tmind ; j++)
			{
				int tmp = j;
				if(tmp == cm.tmind)
					continue;
				if(cm.ActionTable[i][tmp] != null)
					System.out.print(String.format("%5s", cm.ActionTable[i][tmp])+String.format("%5s","|"));
				else
					System.out.print(String.format("%10s", "|"));
			}
			System.out.println("");
		}
		System.out.println("---------------------------------------------------------------------------------------------------");
		

	
		cm.SLR();
	}
	
	public void readComponentAndSLR() throws IOException
	{
		File file = new File("C:\\Users\\강민수\\Documents\\새 폴더\\component.txt");
		FileReader fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);
		String s = "";
		int ind = 0;
		int ind2=0;
		s = br.readLine();
		ind = Integer.parseInt(s);
		for(int i=0 ; i<ind ; i++)
		{
			s = br.readLine();
			rule[i] = s;
			Lrule[i] = s.split("==>")[0].trim();
			Rrulr[i] = s.split("==>")[1].trim();
		}
		s = br.readLine();
		ind = Integer.parseInt(s);
		ntind = ind;
		for(int i=0 ; i<ind ; i++)
		{
			s = br.readLine();
			NT[i] = s;
		}
		s = br.readLine();
		ind = Integer.parseInt(s);
		tmind = ind;
		for(int i=0 ; i<ind ; i++)
		{
			s = br.readLine();
			TM[i] = s;
		}
		s = br.readLine();
		ind = Integer.parseInt(s);
		for(int i=0 ; i<ind ; i++)
		{
			s = br.readLine();
			ind2 = Integer.parseInt(s.split(" ")[1]);
			firstind[i] = ind2;
			for(int j=0 ; j<ind2 ; j++)
			{
				s = br.readLine();
				first[i][j] = s;
			}
		}

		s = br.readLine();
		ind = Integer.parseInt(s);
		for(int i=0 ; i<ind ; i++)
		{
			s = br.readLine();
			ind2 = Integer.parseInt(s.split(" ")[1]);
			fallowind[i] = ind2;
			for(int j=0 ; j<ind2 ; j++)
			{
				s = br.readLine();
				fallow[i][j] = s;
			}
		}
		s = br.readLine();
		ind = Integer.parseInt(s);
		colind = ind;
		for(int i=0 ; i<ind ; i++)
		{
			s = br.readLine();
			ind2 = Integer.parseInt(s.split(" ")[1]);
			canind[i] = ind2;
			for(int j=0 ; j<ind2 ; j++)
			{
				s = br.readLine();
				canset[i][j] = s;
			}
		}
		CreateTable();
		for(int i=0 ; i<colind ; i++)
		{
			s = br.readLine();
			for(int j=0 ; j<s.split(" ").length ; j++)
			{
				if(s.split(" ")[j].equals("-"))
					continue;
				else
					GotoTable[i][j+1] = s.split(" ")[j].trim();
			}
		}
		for(int i=0 ; i<colind ; i++)
		{
			s = br.readLine();
			for(int j=0 ; j<s.split(" ").length ; j++)
			{
				if(s.split(" ")[j].equals("-"))
					continue;
				else
					ActionTable[i][j] = s.split(" ")[j].trim();
			}
		}
		br.close();
		fr.close();
	}

	public static void main(String[] args) throws IOException {

		String a;
		Scanner scan = new Scanner(System.in);

		System.out.println("옵션을 선택해 주세요 : ");

		System.out.println("1번 : 기본 문법 파일을 불러와 테이블을 만들고 저장합니다");
		System.out.println("2번 : 저장된 테이블을 불러옵니다");
		a = scan.nextLine();
		if(a.equals("1"))
		{
			run1();
		}
		else if(a.equals("2"))
		{
			run2();
		}
		
		
	}
	
	public void saveComponent() throws IOException
	{
		BufferedWriter bw = new BufferedWriter(new FileWriter("C:\\Users\\강민수\\Documents\\새 폴더\\component.txt"));
		String s;
		s = Integer.toString(rulrIdx);
		bw.write(s); bw.newLine();
		for(int i=0 ; i<rulrIdx ; i++)
		{
			s = Lrule[i]+" ==> "+Rrulr[i];
			bw.write(s);
			bw.newLine();
		}
		s = Integer.toString(ntind);
		bw.write(s); bw.newLine();
		for(int i=0 ; i<ntind ; i++)
		{
			s = NT[i];
			bw.write(s);
			bw.newLine();
		}
		s = Integer.toString(tmind);
		bw.write(s); bw.newLine();
		for(int i=0 ; i<tmind ; i++)
		{
			s = TM[i];
			bw.write(s);
			bw.newLine();
		}
		s = Integer.toString(ntind);
		bw.write(s);
		bw.newLine();
		for(int i=0 ; i<ntind ; i++)
		{
			s = Integer.toString(i) + " " + Integer.toString(firstind[i]);
			bw.write(s); bw.newLine();
			for(int j=0 ; j<firstind[i] ; j++)
			{
				s = first[i][j];
				bw.write(s);
				bw.newLine();
			}
		}
		s = Integer.toString(ntind);
		bw.write(s);
		bw.newLine();
		for(int i=0 ; i<ntind ; i++)
		{
			s = Integer.toString(i) + " " + Integer.toString(fallowind[i]);
			bw.write(s); bw.newLine();
			for(int j=0 ; j<fallowind[i] ; j++)
			{
				s = fallow[i][j];
				bw.write(s);
				bw.newLine();
			}
		}
		s = Integer.toString(colind);
		bw.write(s);
		bw.newLine();
		for(int i=0 ; i<colind ; i++)
		{
			s = Integer.toString(i) + " " + Integer.toString(canind[i]);
			bw.write(s); bw.newLine();
			for(int j=0 ; j<canind[i] ; j++)
			{
				s = canset[i][j];
				bw.write(s);
				bw.newLine();
			}
		}
		
		for(int i=0 ; i<colind ; i++)
		{
			for(int j=1 ; j<ntind ; j++)
			{
				if(GotoTable[i][j]==null)
				{
					s = "-";
				}
				else
				{
					s = GotoTable[i][j];
				}
				bw.write(s+" ");
			}
			bw.newLine();
		}

		for(int i=0 ; i<colind ; i++)
		{
			for(int j=0 ; j<tmind ; j++)
			{
				if(ActionTable[i][j]==null)
				{
					s = "-";
				}
				else
				{
					s = ActionTable[i][j];
				}
				bw.write(s+" ");
			}
			bw.newLine();
		}
		
		bw.close();
		
		
		
		
	}
	
	public void findpowerset(int data[],int n,int depth,int flag[])
	{
		if(n==depth)
		{
			int i;
			for(i=0 ; i<n ; i++)
			{
				if(flag[i] == 1)
				{
					powerset[psind2][psind1[psind2]] = data[i];
					psind1[psind2]++;
				}
			}
			psind2++;
			return;
		}
		flag[depth]=1;
		findpowerset(data,n,depth+1,flag);

		flag[depth]=0;
		findpowerset(data,n,depth+1,flag);
	}
	
	public void removenullable()
	{
		String[] tmpLrule = (String[])Lrule.clone();
		String[] tmpRrule = (String[])Rrulr.clone();
		int tmpRuleInd = rulrIdx;
		String tmpL;
		int[] ntnt = new int[2];
		int[] indind = new int[500];
		int indindind = 0;
		rulrIdx = 1;
		StringBuffer sb = null;
		
		for(int i=0 ; i<tmpRuleInd ; i++)
		{
			if(i == 0)
				continue;
			indindind = 0;
			tmpL = tmpLrule[i];
			if(tmpRrule[i].equals("__"))
				continue;
			
			for(int j=0 ; j<tmpRrule[i].split(" ").length ; j++)
			{
				ntnt = checknt(tmpRrule[i].split(" ")[j]);
				if(ntnt[0] == 1)
				{
					if(nullable[ntnt[1]])
					{
						indind[indindind] = j;
						indindind++;
					}
				}
			}
			int[] data = new int[indindind];
			int[] flag = new int[indindind];
			for(int j=0 ; j<indindind; j++)
				data[j] = indind[j];
			for(int j=0 ; j<psind2 ; j++)
			{
					psind1[j] = 0;
			}
			psind2=0;
			findpowerset(data,indindind,0,flag);
			for(int j=0 ; j<psind2 ; j++)
			{
				int[] b = new int[psind1[j]];
				String aa[] = new String[psind1[j]];
				int aaind = 0;
				int aaa=0,bbb=0;
				String ttmp = tmpRrule[i];
				sb = new StringBuffer(ttmp);
				for(int x=0 ; x<psind1[j] ; x++)
				{
					aaa=0;
					bbb=0;
					for(int xx=0 ; xx<powerset[j][x] ; xx++)
					{
						aaa = aaa+ttmp.split(" ")[xx].length()+1;
					}
					bbb=aaa+ttmp.split(" ")[powerset[j][x]].length()+1;
					aa[aaind] = ttmp.split(" ")[powerset[j][x]];
					aaind++;
					sb.delete(aaa,bbb);
					if(x<psind1[j]-1)
						powerset[j][x+1]--;
				}
				ttmp = sb.toString();
				if(ttmp.trim().equals(""))
					continue;
				Lrule[rulrIdx] = tmpL;
				Rrulr[rulrIdx] = ttmp.trim();
				rule[rulrIdx] = Lrule[rulrIdx] + " ==> " + Rrulr[rulrIdx];
				rulrIdx++;
				
			}
			
			
		}
		
	}
	
	
	public void CreateTable() {		//goto/action테이블 생성
		ActionTable = new String[500][tmind+1];
		GotoTable = new String[500][ntind+1];
		ActionTable[1][0] = "Acc";
	}
	public void CreateLookAHead()
	{
		lookahead = new String[colind][tmind];
		lahind1 = new int[colind];
		
		
	}
	public boolean RMF(String path) throws FileNotFoundException {
		FileReader grfile = new FileReader(path);
		BufferedReader br = new BufferedReader(grfile);
		FileWriter fw = null;
		BufferedWriter bw = null;
		String str = null;
		String tmp = null;
		String rtmp;
		String tmpp[] = new String[100];
		int tmppind=0;
		
		
		
		
		
		
		
		
		
		// 증가 문법으로 만들고 시작한다
		boolean isnt;
		
		
		try {
			str = br.readLine();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		
		if(!str.split(" ")[0].equals("S'"))
		{
			tmpp[tmppind] = "S' ==> "+str.split(" ")[0];
			tmppind++;
			tmpp[tmppind] = str;
			tmppind++;
			try {
				while((str = br.readLine()) != null)
				{
					tmpp[tmppind]= str;
					tmppind++;
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		
		try {
			br.close();
			grfile.close();
		} catch (IOException e2) {
			// TODO Auto-generated catch block
			e2.printStackTrace();
		}
		
		if(tmpp[0]!=null)
		{
		try {
			fw = new FileWriter(path);
			bw = new BufferedWriter(fw);
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

		for(int i=0 ; i<tmppind ; i++)
		{
			try {
				bw.write(tmpp[i]);
				if(!(i==tmppind-1))
					bw.newLine();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		
		
		try {
			bw.flush();
			fw.close();
			bw.close();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		}
		
		
		
		
		
		grfile =  new FileReader(path);
		br = new BufferedReader(grfile);
		
		try {
			while ((str = br.readLine()) != null) {
				rule[rulrIdx] = new String(str);
				i = 0;
				if (rulrIdx >= 500) {
					System.out.print("규칙이 500개가 넘습니다.");
					try {
						br.close();
					} catch (IOException e) {
						e.printStackTrace();
					}
					return false;
				}
				if (!str.contains("==>")) {/*
											 * tmp = Lrule[rulrIdx-1]; Lrule[rulrIdx] = tmp; if(str.contains("||")) {
											 * 
											 * } else { Rrulr[rulrIdx] = str.trim(); } rulrIdx++;
											 */
				} else if (str.contains("\\|\\|")) {
					tmp = Lrule[rulrIdx] = str.split("==>")[0];
					rtmp = str.split("==>")[1];
					int x = rtmp.split("\\|\\|").length;
					while (x > i) {
						if (i == 0) {
							Rrulr[rulrIdx] = rtmp.split("\\|\\|")[i];
						} else {
							Lrule[rulrIdx] = tmp;
							Rrulr[rulrIdx] = rtmp.split("\\|\\|")[i];
						}
						Lrule[rulrIdx] = Lrule[rulrIdx].trim();
						Rrulr[rulrIdx] = Rrulr[rulrIdx].trim();
						System.out.println("L : " + Lrule[rulrIdx] + ", R : " + Rrulr[rulrIdx]);
						i++;
						rulrIdx++;
					}

				} else {
					Lrule[rulrIdx] = str.split("==>")[0];
					Rrulr[rulrIdx] = str.split("==>")[1];
					Lrule[rulrIdx] = Lrule[rulrIdx].trim();
					Rrulr[rulrIdx] = Rrulr[rulrIdx].trim();
					System.out.println("L : " + Lrule[rulrIdx] + ", R : " + Rrulr[rulrIdx]);
					rulrIdx++;
				}
				// 이하는 논터미널 검출
				if (ntind == 0) {
					NT[ntind] = new String(Lrule[rulrIdx - 1]);
					ntind++;
				} else {
					isnt = true;
					for (i = 0; i < ntind; i++) {
						if (NT[i].equals(Lrule[rulrIdx - 1]))
							isnt = false;
					}
					if (isnt) {
						NT[ntind] = new String(Lrule[rulrIdx - 1]);
						ntind++;
					}
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		try {
			br.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return true;
	}

	public void FT() {
		i = 0;
		String tmp[];
		boolean isft = true;
		TM[tmind] = "$";
		tmind++;
		for (i = 0; i < rulrIdx; i++) {
			tmp = Rrulr[i].split(" ");
			for (int j = 0; j < tmp.length; j++) {
				isft = true;
				for (int k = 0; k < ntind; k++) {
					if (NT[k].equals(tmp[j]))
						isft = false;
				}
				for (int k = 0; k < tmind; k++) {
					if (TM[k].equals(tmp[j]))
						isft = false;
				}
				if(tmp[j].equals("__"))
					isft = false;
				if (isft == true) {
					TM[tmind] = new String(tmp[j]);
					tmind++;
				}
			}
		}
	}

	public void findFirst() {
		String tmp;
		int where = 0;
		boolean isnt = false;
		// 첫번째 순회. 202쪽 2번
		for (int j = 0; j < rulrIdx; j++) {
			tmp = Lrule[j];
			for (int k = 0; k < ntind; k++) // 어느 논터미널인지 찾는것.
			{
				if (tmp.equals(NT[k])) {
					where = k;
					break;
				}
			}
			tmp = Rrulr[j].split(" ")[0];
			for (int k = 0; k < ntind; k++) {
				isnt = false;
				if (tmp.equals(NT[k])) {
					isnt = true;
					break;
				}
			}
			if (!isnt) {
				first[where][firstind[where]] = tmp;
				firstind[where]++;
			}
		}

		// 두번째 순회 202쪽 4번

		int where2 = 0;
		where = 0;
		int gg;
		String[] tmp2 = new String[100];
		boolean same = false;
		boolean isit = false;
		int fl = 0;

		String[][] firtmp = new String[500][100];
		for (int j = 0; j < ntind; j++) {
			for (int k = 0; k < firstind[j]; k++) {
				firtmp[j][k] = new String(first[j][k]);
			}
		}
		boolean isnullable = false;
		while (true) {
			same = true;
			for (int j = 0; j < rulrIdx; j++) {
				isnullable = false;
				tmp = Lrule[j];
				for (int k = 0; k < ntind; k++) // 어느 논터미널인지 찾는것.
				{
					if (tmp.equals(NT[k])) {
						where = k;
						break;
					}
				}
				tmp2 = Rrulr[j].split(" ");
				for (int k = 0; k < tmp2.length; k++) {
					isnt = false;
					isnullable = false;
					for (int x = 0; x < ntind; x++) // 어느 논터미널인지 찾는것.
					{
						if (tmp2[k].equals(NT[x])) {
							where2 = x;
							isnt = true;
							break;
						}
					}
					if (isnt) {
						for (int c = 0; c < firstind[where2]; c++) {
							fl = 0;
							gg = 0;
							isit=false;
							for (gg = 0; gg < firstind[where]; gg++) {
								if (first[where2][c].equals(first[where][gg])) {
									isit = true;
									break;
								}
							}
							if (isit) {

							} else {
								first[where][firstind[where]] = new String(first[where2][c]);
							}
							while (true) {
								if (first[where][fl] == null) {
									break;
								}
								fl++;
							}
							if (firstind[where] == fl) {
							} else
								firstind[where]++;
							if (first[where2][c].contains("__"))
								isnullable = true;
						}
					}
					if (isnullable)
						continue;
					else
						break;
				}
			}
			// 계속해서 반복한다음 변화가 없을때 종료.

			for (int g = 0; g < ntind; g++) {
				for (int f = 0; f < firstind[g]; f++) {
					if (!first[g][f].equals(firtmp[g][f])) {
						same = false;
						break;
					}
				}
			}
			if (same)
				break;
			for (int g = 0; g < ntind; g++) {
				for (int f = 0; f < firstind[g]; f++) {
					firtmp[g][f] = new String(first[g][f]);
				}
			}
		} // while끝
	}

	public void findnullable()
	{
		int x=0;
		int lwhere = 0;
		int rwhere = 0;
		boolean nulltmp[] = new boolean[500];
		boolean same = true;
		String tmp[];
		String ltmp = null;
		boolean isnt = false;
		for(int j=0 ; j<rulrIdx ; j++)
		{
			for(x=0 ; x<ntind ; x++)
			{
				if(Lrule[j].equals(NT[x]))
					break;
			}
			if(Rrulr[j].equals("__"))
			{
				nulltmp[x] = nullable[x] = true;
			}
		}
		while(true)
		{
			for(int g = 0 ; g<rulrIdx ; g++)
			{
				ltmp = Lrule[g];
				for(int c = 0 ; c<ntind ; c++)
				{
					if(ltmp.equals(NT[c]))
					{
						lwhere = c;
						break;
					}
				}
				tmp = Rrulr[g].split(" ");
				for(int c = 0 ; c<tmp.length ; c++)
				{
					isnt = false;
					for(int v=0 ; v<ntind ; v++)
					{
						if(tmp[c].equals(NT[v]))
						{
							isnt = true;
							rwhere = v;
							break;
						}
					}
					if(!isnt)
						break;
					if(tmp.length ==1)
					{
						if(nullable[rwhere] == true)
							nullable[lwhere] = true;
					}
					else
					{
						if(nullable[rwhere] == true)
							continue;
						else
							break;
					}
				}
			}
			
			same = true;
			
			for(int g = 0; g<ntind ; g++)
			{
				if(nulltmp[g] != nullable[g])
				{
					same = false;
					break;
				}
			}
			if(same)
				break;
			for(int g = 0; g<ntind ; g++)
			{
				nulltmp[g] = nullable[g];
			}
			
		}
		
		
		x=1;
		x=0;
	}
	
	public void findFallow() {
		fallow[0][0] = new String("$");		//스타트심볼의 팔로우는 무조건 $가 들어간다
		fallowind[0]++;
		boolean same = true;
		String fallowtmp[][] = new String[500][100];
		findnullable();
		String[] rtmp;
		String ltmp;
		boolean isnt = false;
		boolean isnt2 = false;
		int rwhere2=0;
		boolean na = false;
		boolean isit = false;
		int lwhere=0,rwhere=0;
		while(true)
		{
			for(int g=0 ; g<rulrIdx ; g++)
			{
				ltmp = Lrule[g];
				for(int c = 0; c<ntind ; c++)	//왼쪽 어디
				{
					if(ltmp.equals(NT[c]))
					{
						lwhere = c;
						break;
					}
				}
				rtmp = Rrulr[g].split(" ");
				if(rtmp.length == 1)			//오른쪽규칙이 한개일때
				{
					for(int cc=0 ; cc<ntind ; cc++)
					{
						if(rtmp[0].equals(NT[cc]))
						{
							isnt = true;
							rwhere = cc;
							break;
						}
					}
					if(isnt)		//오른쪽이 논터미널,터미널일때는 아무것도 안해도 된다
					{
						isit = false;
						for(int cc=0 ; cc<fallowind[lwhere] ; cc++)
						{
							for(int ccc=0 ; ccc<fallowind[rwhere] ; ccc++)
							{
								if(fallow[lwhere][cc].equals(fallow[rwhere][ccc]))
								{
									isit = true;
									break;
								}
							}
							if(!isit)
							{
								fallow[rwhere][fallowind[rwhere]] = new String(fallow[lwhere][cc]);
								fallowind[rwhere]++;
							}
						}
					}
					continue;
				}
				for(int c=rtmp.length-1 ; c>0 ; c--)
				{
					isnt=false;
					isnt2 = false;
					rwhere = 0;
					rwhere2 = 0;
					
					
					for(int cc=0 ; cc<ntind ; cc++)
					{
						if(rtmp[c-1].equals(NT[cc]))
						{
							isnt = true;
							rwhere = cc;
							break;
						}
					}
					for(int cc=0 ; cc<ntind ; cc++)
					{
						if(rtmp[c].equals(NT[cc]))
						{
							isnt2 = true;
							rwhere2 = cc;
							break;
						}
					}
					if(isnt2 == false)		//뒤가 터미널
					{
						if(isnt == false)		//앞이 터미널
							continue;
						else				//앞이 논터미널
						{
							if(rtmp[c] == "__" )
								continue;
							isit=false;
							for(int h=0 ; h<fallowind[rwhere] ; h++)
							{
								if(rtmp[c].equals(fallow[rwhere][h]))
									isit = true;
							}
							if(isit == false)
							{
								fallow[rwhere][fallowind[rwhere]] = new String(rtmp[c]);
								fallowind[rwhere]++;
							}
						}
					}
					else		//뒤가 논터미널
					{
						if(c == rtmp.length-1)	//맨끝일때
						{
							for(int h=0 ; h<fallowind[lwhere] ; h++)
							{
								isit = false;
								for(int cc=0 ; cc<fallowind[rwhere2] ; cc++)
								{
									if(fallow[rwhere2][cc].equals(fallow[lwhere][h]))
									{
										isit = true;
										break;
									}
								}
								if(isit == false)
								{
									fallow[rwhere2][fallowind[rwhere2]] = new String(fallow[lwhere][h]);
									fallowind[rwhere2]++;
								}
							}
							if(isnt == false)		//앞이 터미널
							{
								continue;
							}
							for(int gx = 0 ; gx < firstind[rwhere2] ; gx++)
							{
								isit = false;
								for(int ge = 0 ; ge<fallowind[rwhere] ; ge++)
								{
									if(fallow[rwhere][ge].equals(first[rwhere2][gx]))
									{
										isit = true;
										break;
									}
								}
								if(isit == false && !first[rwhere2][gx].equals("__"))
								{
									fallow[rwhere][fallowind[rwhere]]  = new String(first[rwhere2][gx]);
									fallowind[rwhere]++;
								}
							}
						}
						else		//맨끝이 아닐때
						{
							for(int gx = 0 ; gx < firstind[rwhere2] ; gx++)
							{
								isit = false;
								for(int ge = 0 ; ge<fallowind[rwhere] ; ge++)
								{
									if(fallow[rwhere][ge].equals(first[rwhere][gx]))
									{
										isit = true;
										break;
									}
								}
								if(isit == false)
								{
									fallow[rwhere][fallowind[rwhere]]  = new String(first[rwhere2][gx]);
								}
							}
						}
						na = false;
						for(int gx = rtmp.length-1 ; gx>=c ; gx--)
						{
							for(int ii=0 ; ii<ntind ; ii++)
							{
								if(NT[ii].equals(rtmp[gx]))
								{
									na = true;
									break;
								}
							}
							if(na)
								break;
						}
						if(!na)
							continue;
						int qwer=0;
						na = true;
						for(int gx = rtmp.length-1 ; gx>=c ; gx--)
						{
							for(int cc=0 ; cc<ntind ; cc++)
							{
								if(rtmp[gx].equals(NT[cc]))
								{
									qwer = cc;
									break;
								}
							}
							if(!nullable[qwer])
							{
								na = false;
								break;
							}
						}
						if(!na)
							continue;

						for(int h=0 ; h<fallowind[lwhere] ; h++)
						{
							isit = false;
							for(int cc=0 ; cc<fallowind[rwhere] ; cc++)
							{
								if(fallow[rwhere][cc].equals(fallow[lwhere][h]))
								{
									isit = true;
									break;
								}
							}
							if(isit == false)
							{
								fallow[rwhere][fallowind[rwhere]] = new String(fallow[lwhere][h]);
								fallowind[rwhere]++;
							}
						}
					}
				}
			}
			
			
			
			
			
			//검출항목. 퍼ㅗ스트라ㅓㅇ 똑같음
			same = true;
			for (int g = 0; g < ntind; g++) {
				for (int f = 0; f < firstind[g]; f++) {
					if (!first[g][f].equals(fallowtmp[g][f])) {
						same = false;
						break;
					}
				}
			}
			if (same)
				break;
			for (int g = 0; g < ntind; g++) {
				for (int f = 0; f < firstind[g]; f++) {
					fallowtmp[g][f] = new String(first[g][f]);
				}
			}
		}
	}
	
	public String[] closureCLR(int wherelook,String what1,int ffgg,int ffind)		//wherelook 어디서 보는지 //what = 쩜 다음에 있는 거 // ffgg : canind 때문 // firstind 는 전에 봤던 퍼스트들을 넣어주기 위해 필요함
	{
		boolean same;
		boolean ss;
		int find;
		int reind = 0;
		String[] result = new String[500];
		String[] retmp = new String[500];
		String[] fefe = new String[500];
		String retmpp;
		int fefeind=0;
		String tmp;
		int wheredot = 0;
		boolean isitnul = false;
		int idn = 0;
		int loc = 0;
		String tmpp = null;
		StringBuffer sb = null;
		boolean isit = false;
		int dotwhere = 0;
		boolean isnt = false;
		int ntwhere = 0;
		String what = null;
		boolean cor = false;
		int[] ntnt = new int[2];
		

		Queue<String> qu = new LinkedList<String>();
		qu.offer(what1);
		
		
		Queue<Integer> qu2 = new LinkedList<Integer>();
		qu2.offer(ffind);

		what = qu.poll();
		for(int i=0 ; i<canind[wherelook] ; i++)
		{
			cor = false;
			for(int j=0 ; j<canset[wherelook][i].split("\\^\\^")[0].split(" ").length ; j++)
			{
				if(canset[wherelook][i].split("\\^\\^")[0].split(" ")[j].equals("."))
				{
					if(j == canset[wherelook][i].split("\\^\\^")[0].split(" ").length-1)
						break;
					if(canset[wherelook][i].split("\\^\\^")[0].split(" ")[j+1].equals(what))
					{
						cor = true;
						break;
					}
				}
			}
			if(cor)
			{
				//점을 옮겨
				tmp = canset[wherelook][i].split("\\^\\^")[0];
				loc = tmp.indexOf(".");
				loc = loc + what.length(); 
				tmpp = tmp.replace(" .", "");
				sb = new StringBuffer(tmpp);
				sb.setLength(sb.length()+3);
				sb.insert(loc," .");
				tmpp = sb.toString().trim();
				//lookahead를 취해
				for(int j=0 ; j<tmpp.split(" ").length ; j++)
				{
					if(tmpp.split(" ")[j].equals("."))
					{
						dotwhere = j;
						break;
					}
				}
				if(dotwhere == tmpp.split(" ").length-1)
				{
					tmpp = tmpp+" ^^&";
				}
				else
				{
					ntnt = checknt(tmpp.split(" ")[dotwhere+1]);
					if(ntnt[0] == 1)	//논터미널
					{
						tmpp = tmpp+" ^^"+first[ntnt[1]];
						qu.offer(tmpp.split(" ")[dotwhere+1]);
					}
					else
					{
						tmpp = tmpp+" ^^"+TM[ntnt[1]];
					}
				}
				result[reind] = new String(tmpp);
				reind++;
			}
		}
		
		while(true)
		{
			ss = true;
			while(!qu.isEmpty())
			{
				
			}
			
			same = true;
			for(int i=0 ; i<reind ; i++)
			{
				if(!result[i].equals(retmp[i]))
				{
					same = false;
					break;
				}
			}
			if(same)
				break;
			for(int i=0 ; i<reind ; i++)
			{
				retmp[i] = new String(result[i]);
			}
		}
		canind[ffgg] = reind;
		return result;
	}

	public String[] closure(int wherelook,String bb,int ffgg)					//wherelook : 어디서 보고있는지 / what : 무엇을 보는지
	{
		String[] result = new String[500];
		int reind = 0;
		String[] retmp = new String[500];
		boolean same = false;
		String tmp;
		StringBuffer sb;
		String tmpp = null;
		int loc = 0;
		int idn = 0;
		boolean isit = true;
		boolean isnt = true;
		int dotwhere=0;
		String ne = null;
		String what = new String(bb);
		Queue<String> qu = new LinkedList<String>();
		qu.offer(what);
		boolean ss=true;
		String retmpp = null;
		int wd = 0;
		boolean fdfd = false;
		String[] fefe = new String[100];
		int fefeind = 0;
		int xxx = 0;
		boolean fefefe = false;
		
		while(true)
		{
			ss = true;
			while(!qu.isEmpty())
			{
				fefe[fefeind] = what = qu.poll();
				fefeind++;
				if(!ss)
				{
					for(int i=0 ; i<canind[0] ; i++)
					{
						if(canset[0][i].split(" ")[0].equals(what))
						{
							retmpp = result[reind] = new String(canset[0][i]);
							reind++;
							
							for(int xx=0 ; xx<retmpp.split(" ").length ; xx++)
							{
								if(retmpp.split(" ")[xx].equals("."))
								{
									wd = xx;
									break;
								}
							}
							fdfd = false;
							fefefe = true;
							for(int xx=0 ; xx<ntind ; xx++)
							{
								if(retmpp.split(" ")[wd+1].equals(NT[xx]))
								{
									xxx = xx;
									fdfd = true;
									break;
								}
							}
							for(int xx=0 ; xx<fefeind ; xx++)
							{
								if(retmpp.split(" ")[wd+1].equals(fefe[xx]))
								{
									xxx = xx;
									fefefe = false;
									break;
								}
							}
							if(fdfd && fefefe)
							{
								qu.offer(retmpp.split(" ")[wd+1]);
							}
						}
					}
				}
				
				
				else
				{
				for(int i=0 ; i<canind[wherelook] ; i++)
				{
					tmp = canset[wherelook][i];
					for(int j=0 ; j<tmp.split(" ").length ; j++)
					{
						idn = -1;
						if(tmp.split(" ")[j].equals("."))
						{
							idn = j+1;
						}
						if(idn == tmp.split(" ").length)
							idn--;
						if(idn == -1)
							continue;
						if(tmp.split(" ")[idn].equals(what))
						{
							loc = tmp.indexOf(".");
							loc = loc + what.length(); 
							tmpp = tmp.replace(" .", "");
							sb = new StringBuffer(tmpp);
							sb.setLength(sb.length()+3);
							sb.insert(loc," .");
							tmpp = sb.toString().trim();
							
							isit = false;
							for(int k=0 ; k<reind ; k++)
							{
								if(result[k].equals(tmpp))
								{
									isit = true;
									break;
								}
							}
							if(!isit)
							{
								result[reind] = tmpp;
								reind++;
								for(int xx=0 ; xx<tmpp.split(" ").length ; xx++)
								{
									if(tmpp.split(" ")[xx].equals("."))
									{
										dotwhere = xx;
									}
								}
								if(dotwhere == tmpp.split(" ").length-1)
									continue;
								isnt = false;
								for(int xx=0 ; xx<ntind ; xx++)
								{
									if(tmpp.split(" ")[dotwhere+1].equals(NT[xx]))
									{
										isnt = true;
										break;
									}
								}
								if(isnt)
								{
									qu.offer(tmpp.split(" ")[dotwhere+1]);
									ss = false;
									break;
								}
							}
						}
					}
				}//for끝
				}
			}//while끝
			
			
			
			
			
			same = true;
			for(int i=0 ; i<reind ; i++)
			{
				if(!result[i].equals(retmp[i]))
				{
					same = false;
					break;
				}
			}
			if(same)
				break;
			for(int i=0 ; i<reind ; i++)
			{
				retmp[i] = new String(result[i]);
			}
		}
		canind[ffgg] = reind;
		return result;
	}
	
	
	public int[] checknt(String sym)
	{
		int result[] = new int[2];
		for(int i=0 ; i<ntind ;i++)
		{
			if(sym.equals(NT[i]))
			{
				result[0] = 1;
				result[1] = i;
				return result;
			}
		}
		for(int i=0 ; i<tmind ; i++)
		{
			if(sym.equals(TM[i]))
			{
				result[0] = 0;
				result[1] = i;
				return result;
			}
		}
		result[0] = -1;
		result[1] = -1;
		return result;
	}
	
	
	public void canonicalsetCLR()
	{
		Queue<String> qu = new LinkedList<String>();
		Queue<String> lah = new LinkedList<String>();
		String Rtmp;
		String Ltmp;
		String lahsimbol;
		String Rule;
		int ntnt[] = new int[2];
		int wheredot = 0;
		int loc;
		StringBuffer sb;
		int w = 0;
		int sple;
		Rtmp = Rrulr[0];
		Ltmp = Lrule[0];
		Rule = Ltmp + " ==> . " + Rtmp;
		for(int j=0 ; j<Rule.split(" ").length ; j++)
		{
			if(Rule.split(" ")[j].equals("."))
			{
				wheredot = j;
				break;
			}
		}
		if((wheredot != Rule.split(" ").length-1))
		{
			qu.offer(Rule.split(" ")[wheredot+1]);
			if(wheredot == Rule.split(" ").length-2)
			{
				lah.offer("$");
			}
			else
			{
				lahsimbol = Rule.split(" ")[wheredot+2];
				ntnt = checknt(lahsimbol);
				if(ntnt[0] == 1)
				{
					String lahtmp= "";
					for(int i=0 ; i<firstind[ntnt[1]] ; i++)
					{
						lahtmp += first[ntnt[1]][i];
					}
					lah.offer(lahtmp);
				}
				else
				{
					lah.offer(lahsimbol);
				}
			}
		}
		Rule = Rule + " ^^$";	//처음엔 $를 넣어줌
		canset[colind][canind[colind]] = Rule;
		canind[colind]++;
		boolean isit = false;
		while(!qu.isEmpty())
		{
			Ltmp = qu.poll();
			lahsimbol = lah.poll();
			for(int i=0 ; i<rulrIdx ; i++)
			{
				if(Lrule[i].equals(Ltmp))
				{
					Rtmp = Rrulr[i];
					Rule = Ltmp + " ==> . " + Rtmp + " ^^"+lahsimbol;
					isit = false;
					for(int j=0 ; j<canind[colind] ; j++)
					{
						if(canset[colind][j].equals(Rule))
						{
							isit = true;
							break;
						}
					}
					if(isit)
						continue;
					isit = false;
					for(int j=0 ; j<canind[colind] ; j++)
					{
						String a;
						String b;
						a = canset[colind][j].split("\\^\\^")[0];
						b = Rule.split("\\^\\^")[0];
						if(a.equals(b))
						{
							//정렬필요할수도있음
							canset[colind][j] += Rule.split("\\^\\^")[1];
							isit = true;
						}
					}
					if(isit)
						continue;
					canset[colind][canind[colind]] = Rule;
					canind[colind]++;
					wheredot = 0;
					for(int j=0 ; j<Rule.split(" ").length ; j++)
					{
						if(Rule.split(" ")[j].equals("."))
						{
							wheredot = j;
							break;
						}
					}
					

					if((wheredot != Rule.split(" ").length-2))
					{
						
						ntnt = checknt(Rule.split(" ")[wheredot+1]);
						if(ntnt[0] == 1)
						{
							qu.offer(Rule.split(" ")[wheredot+1]);
						}
						else
						{
							continue;
						}
						if(wheredot == Rule.split(" ").length-3)
						{
							lah.offer("$");
						}
						else
						{
							String lahsimbol1 = Rule.split(" ")[wheredot+2];
							ntnt = checknt(lahsimbol1);
							if(ntnt[0] == 1)
							{
								String lahtmp= "";
								for(int x=0 ; x<firstind[ntnt[1]] ; x++)
								{
									lahtmp += first[ntnt[1]][x];
								}
								lah.offer(lahtmp);
							}
							else
							{
								lah.offer(lahsimbol1);
							}
						}
					}
				}
			}
		}
		colind++;
		
		//0번 구성요소 완료
		//이제부터 시작..
		boolean same = false;
		int wherelook = 0;
		qu.clear();
		lah.clear();
		while(true)
		{
			
			if(same)
			{
				break;
			}
		}
	}
	
	
	public void canonicalset()
	{
		String tmp = null;
		String tmp2 = null;
		String tmpp2 = null;
		Queue<String> qu = new LinkedList<String>();
		String sr[] = new String[100];
		StringBuffer sb;
		int srind = 0;
		int loc;
		int w=0;
		boolean isit = false;
		for(int i=0 ; i<rulrIdx ; i++)
		{
			tmpp2 =  Lrule[i];
			tmp2 = Rrulr[i];
			tmp = tmpp2 + " ==> " + tmp2;
			loc = tmp.indexOf("==> ") + "==> ".length();
			sb = new StringBuffer(tmp);
			sb.insert(loc, ". ");
			tmp = sb.toString();
			canset[colind][canind[colind]] = tmp;
			canind[colind]++;
			kernel[kerind] = tmp;
			kerind++;
			for(int j=0 ; j<tmp.split(" ").length ; j++)
			{
				if(tmp.split(" ")[j].equals("."))
				{
					w=j+1;
					break;
				}
			}
			isit = false;
			for(int k=0 ; k<srind ; k++)
			{
				if(sr[k].equals(tmp.split(" ")[w]))
				{
					isit = true;
					break;
				}
			}
			if(!isit)
			{
				sr[srind] = tmp.split(" ")[w];
				qu.offer(tmp.split(" ")[w]);
				srind++;
			}
		}
		sr = null;
		colind++;
		String nent = null;
		int wherelook = 0;
		int wd = 0;
		int wdd = 0;
		int ntnt[] = new int[2];
		String gdgd;
		String gdgdd;
		String grgr;
		int rrr = 0;
		int wnt=0;
		int ppp = 0;
		while(wherelook<=colind)
		{
			int qwer=1;
			qwer=2;
			
			while(!qu.isEmpty())
			{
				//goto에 추가..
				nent = qu.poll();
				canset[colind] = closure(wherelook,nent,colind);
				ntnt = checknt(nent);
				//nent가 논터미널이면 gotoTable에 넣어준다
				//...
				if(ntnt[0] == 1)
				{
					GotoTable[wherelook][ntnt[1]] = "q"+colind;
				}
				//nent가 터미널이면 actionTable에 넣어준다
				//..
				else if(ntnt[0] == 0)
				{
					//if(ActionTable[wherelook][ntnt[1]] == null)
						ActionTable[wherelook][ntnt[1]] = "s"+colind;
				}
				//만약 맨끝을 보고있다면
				for(int i=0 ; i<canind[colind] ; i++)
				{
					gdgd = canset[colind][i];
					for(int j=0 ; j<gdgd.split(" ").length ; j++)
					{
						if(gdgd.split(" ")[j].equals("."))
						{
							rrr = j;
							break;
						}
					}
					if(rrr == gdgd.split(" ").length-1)		//맨끝을 보고있다면
					{
						grgr = gdgd.split(" ")[0];
						if(grgr.equals("S'"))
							continue;
						for(int j=0 ; j< ntind ; j++)
						{
							if(grgr.equals(NT[j]))
							{
								wnt = j;
								break;
							}
						}
						for(int j=0 ; j<fallowind[wnt] ; j++)
						{
							
							ntnt = checknt(fallow[wnt][j]);
							//if(ActionTable[colind][ntnt[1]] != null)
							//	continue;
							gdgd = gdgd.replace(" .","");
							for(int r=0 ; r<rulrIdx ; r++)
							{
								gdgdd = rule[r];
								if(gdgd.equals(gdgdd))
								{
									ppp = r;
									break;
								}
							}
							if(ActionTable[colind][ntnt[1]] != null)
								ActionTable[colind][ntnt[1]] = "r"+ppp;
							else
								ActionTable[colind][ntnt[1]] = "r"+ppp;
						}
					}
				}
				//goto테이블에 리듀스액션을 넣어준다(왼쪽 생성규칙에 fallow들이 index)
				colind++;
			}
			wherelook++;
			for(int i=0 ; i<canind[wherelook] ; i++)	//지금 보고있는것을 줄별로 검출
			{
				tmp = canset[wherelook][i];
				wd = -1;
				isit = false;
				for(int j=0 ; j<tmp.split(" ").length ; j++)//마크의 위치를 검출
				{
					if(tmp.split(" ")[j].equals("."))
					{
						wd = j;
						break;
					}
				}
				if(wd == -1 || wd == tmp.split(" ").length - 1)//마크가 맨 끝에있으면(더이상 볼게 없으면)
				{
					continue;									//다음줄로
				}
				
				
				String xxdd = new String(tmp.split(" ")[wd+1]);
				isit = false;
				int lind=0,rind = 0;
				String L[] = new String[100];
				String R[] = new String[100];
				int li=0,ri;
				wdd = 0;
				ri=0;
				rind=0;
				int x = 0;
				//중복검사
				
				for(int gg1 = 0 ; gg1<canind[wherelook] ; gg1++)//지금 보고있는 항목에서 tmp와 같은걸 보고있는 항목을 전부 빼옴
				{
					for(int ggg1=0 ; ggg1<canset[wherelook][gg1].split(" ").length ; ggg1++)
					{
						if(canset[wherelook][gg1].split(" ")[ggg1].equals("."))
						{
							wdd = ggg1;
							break;
						}
					}
					if( canset[wherelook][gg1].split(" ").length-1 != wdd&&xxdd.equals(canset[wherelook][gg1].split(" ")[wdd+1]) )
					{
						R[rind] = canset[wherelook][gg1];
						rind++;
					}
				}
				
				//현재까지 본것들중에.
				for(int g=0 ; g<wherelook ;g++ )
				{
					li=0;
					lind=0;
					for(int gg = 0 ; gg<canind[g] ; gg++)
					{
						//canset[g]에 있는 항목들중에 지금 tmp와 같은걸 보고있는 항목을 전부 빼옴
						for(int ggg1=0 ; ggg1<canset[g][gg].split(" ").length ; ggg1++)
						{
							if(canset[g][gg].split(" ")[ggg1].equals("."))
							{
								wdd = ggg1;
								break;
							}
						}
						if(wdd!=canset[g][gg].split(" ").length-1 && xxdd.equals(canset[g][gg].split(" ")[wdd+1]))
						{
							L[lind] = canset[g][gg];
							lind++;
						}
					}
					if(rind != lind)
					{
						continue;
					}
					boolean[] a = new boolean[rind];
					for(int g2=0 ; g2<rind ; g2++)
					{
						a[g2] = false;
						for(int gg=0 ; gg<lind ; gg++)
						{
							if(R[g2].equals(L[gg]))
							{
								a[g2] = true;
								break;
							}
						}
					}
//g = goto
					isit = true;
					for(int g2=0 ; g2<rind ; g2++)
					{
						isit  = isit && a[g2];
					}
					
					if(isit)
					{
						//이미 발견됬다는 뜻이므로 goto 에 추가..
						x = g;
						String gggg;
						ntnt = checknt(tmp.split(" ")[wd+1]);
						if(ntnt[0] == 1)		//논터미널
						{
							gggg = GotoTable[g][ntnt[1]];
							GotoTable[wherelook][ntnt[1]] = gggg;
						}
						else if(ntnt[0] == 0)
						{
							gggg = ActionTable[g][ntnt[1]];
							if(ActionTable[wherelook][ntnt[1]] == null)
								ActionTable[wherelook][ntnt[1]] = gggg;
						}
						break;
					}
				}
				if(isit)
				{
				}
				
				if(!qu.contains(tmp.split(" ")[wd+1]) && !isit)
				{
					qu.offer(tmp.split(" ")[wd+1]);
				}
			}
		}
	}
 
	
	public void removereduce()
	{
		StringBuffer sb;
		for(int i=0 ; i<tmind ; i++)
		{
			for(int j=0 ; j<colind ; j++)
			{
				if(ActionTable[j][i] == null)
					continue;
				else
				{
					//if(ActionTable[j][i].length() > 2)
					//{
						if(ActionTable[j][i].contains("r"))
						{
							/*sb = new StringBuffer(ActionTable[j][i]);
							int x = sb.indexOf("r");
							sb.delete(x, sb.length());
							ActionTable[j][i] = sb.toString();
							if(ActionTable[j][i].length() == 0)*/
								ActionTable[j][i] = null;
						}
						
					//}
					//else
					//	continue;
				}
			}
		}
		ActionTable[1][0] = null;
	}
	
	
	
	public void SLR()
	{
		int step = 0;
		String StackTop = null;
		int Stackt;
		String Action = null;
		int r_ind,c_ind;
		int cnt[] = new int[2];
		int currentstep=0;
		
		Scanner sc = new Scanner(System.in);
		String ints;
		int ind = 0;
		input = sc.nextLine();
		int st = 0;
		int[] ggg;
		long time = System.currentTimeMillis(); 

		SimpleDateFormat dayTime = new SimpleDateFormat("yyyy-mm-dd hh:mm:ss");

		String str = dayTime.format(new Date(time));

		System.out.println("-------------------------------------------------------------------------------");
		System.out.println("Input String : "+input+"\t\t\tDate : "+dayTime.format(new Date(time)));
		System.out.println("-------------------------------------------------------------------------------");
		input = input+" $";
		stack.push("0");
		int p=0;
		System.out.println("[Step Number]\t\t[Stack State]\t\t[Input Buffer]\t\t[Action]");
		while(!stack.isEmpty() || ind>=input.split(" ").length-1)
		{
			st = stack.size()-1;
			StackTop = stack.get(st);
			cnt = checknt(StackTop);
			if(cnt[0] == 1)
			{
				r_ind = Integer.valueOf(stack.get(st-1));
				c_ind = cnt[1];
				if(c_ind == -1)
				{
					showstep(currentstep,"error","error");
					System.exit(1);
				}
				String state = GotoTable[r_ind][c_ind];
				showstep(currentstep,"GOTO",state);
				dogoto(state);
			}
			else
			{
				ggg = checknt(input.split(" ")[cur_input_ptr]);
				c_ind = ggg[1];
				Stackt = Integer.valueOf(stack.get(st));
				if(c_ind == -1)
				{
					showstep(currentstep,"error","error");
					System.exit(1);
				}
				Action = ActionTable[Stackt][c_ind];
				if(Action == null)
				{

					showstep(currentstep,"error","error");
					break;
				}
					
				if(Action.equals("Acc"))
				{
					showstep(currentstep,"Accept","Accept");
					break;
				}
				else if(Action.charAt(0) == 's')
				{
					showstep(currentstep,"Shift",Action);
					//p = Action.charAt(1) - 48;
					p = Integer.parseInt(Action.substring(1, Action.length()));
					doshift(p);
				}
				else if(Action.charAt(0) == 'r')
				{
					showstep(currentstep,"Reduce",Action);
					//p = Action.charAt(1) - 48;
					p = Integer.parseInt(Action.substring(1, Action.length()));
					doreduce(p);
				}
				else
				{
					showstep(currentstep,"error","error");
					break;
				}
			}
			

			currentstep++;
		}
		
		
		
	}
	
	
	public void showstep(int stepNumber,String action,String actionState)
	{
		int size=0;
		for(int i=0 ; i<cur_input_ptr ; i++)
		{
			size += input.split(" ")[i].length()+1;
		}
		String inputBuffer = input.substring(size,input.length());
		String printStack;
		String printPtrStack;
		int idx;
		printStack = stack.toString();
		printStack = printStack.replace("[","");
		printStack=printStack.replace("]","");
		printStack=printStack.replace(",","");
		printStack=printStack.replace(" ","");

		//System.out.println(stepNumber+"\t\t\t"+printStack+"\t\t\t"+inputBuffer+"\t\t"+action+" "+actionState);
		System.out.format("%10s\t%21s\t%22s\t%13s %s\n", stepNumber,printStack,inputBuffer,action,actionState);
		
	}
	public void dogoto(String state1)
	{
		state1 = state1.substring(1, state1.length());
		stack.push(state1);
	}
	
	public void doshift(int state)
	{
		int size=0;
		for(int i=0 ; i<cur_input_ptr ; i++)
		{
			size += input.split(" ")[i].length()+1;
		}
		String input1;
		
		input1 = input.substring(size,size+input.split(" ")[cur_input_ptr].length());
		input1 = input1.trim();
		cur_input_ptr++;
		stack.push(input1);
		stack.push(String.valueOf(state));
	}
	public void doreduce(int state)
	{
		String le = Lrule[state];
		String ri = Rrulr[state];
		for(int i=0; i<ri.split(" ").length ; i++)
		{
			stack.pop();		//번호 빼줌
			tree[treeind] = stack.pop();		//스택에 들어가있는 nonterminal빼줌
			
			treeind++;
		}
		stack.push(le);
	}
}